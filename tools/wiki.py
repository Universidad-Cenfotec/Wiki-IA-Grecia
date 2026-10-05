#!/usr/bin/env python3
"""Search, verify, and stage sources for the Markdown wiki. Standard library only."""
import argparse, collections, csv, datetime, hashlib, json, re, shutil, sys, unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]

def normalize(text):
 return re.sub(r'\s+',' ',unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode().casefold()).strip()

def read_json(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))

def search(query,limit):
 terms=normalize(query).split()
 if not terms:raise ValueError('Escriba al menos una palabra de búsqueda.')
 matches=[]
 for file in sorted((ROOT/'wiki').rglob('*.md')):
  text=file.read_text(encoding='utf-8')
  body=text.split('---',2)[-1] if text.startswith('---\n') else text
  lines=body.splitlines();title=next((l[2:] for l in lines if l.startswith('# ')),file.stem)
  n=normalize(text);present=sum(t in n for t in terms)
  if not present:continue
  score=present*100+sum(min(n.count(t),15) for t in terms)+sum(8 for t in terms if t in normalize(title))
  # Prefer curated pages when relevance is comparable; never search restricted originals.
  if file.parent.name in ('sintesis','casos','consultas','oportunidades'):score+=10
  snippet=next((l for l in lines if not l.startswith(('#','---','actualizada:','titulo:','tipo:')) and all(t in normalize(l) for t in terms)),None)
  if snippet is None:snippet=next((l for l in lines if not l.startswith(('#','---')) and any(t in normalize(l) for t in terms)),title)
  matches.append((score,str(file.relative_to(ROOT)),title,snippet[:420]))
 for _,path,title,snippet in sorted(matches,key=lambda x:(-x[0],x[1]))[:limit]:
  print(title);print(path);print(snippet);print()
 if not matches:print('Sin coincidencias. Pruebe conceptos relacionados o lea index.md.')

def validate():
 errors=[];warnings=[];link_count=0;anchor_count=0
 files=list(ROOT.rglob('*.md'));ids={};anchors={}
 for file in files:
  text=file.read_text(encoding='utf-8')
  anchors[file.resolve()]=set(re.findall(r'<a id="([^"]+)"',text))
  if file.relative_to(ROOT).parts[0]=='wiki' and not text.startswith('---\n'):errors.append('Sin metadatos '+str(file.relative_to(ROOT)))
 for file in files:
  text=file.read_text(encoding='utf-8')
  for target in re.findall(r'\]\(([^\s)]+)\)',text):
   if re.match(r'^(?:https?://|mailto:|app:|oai-library:|sandbox:)',target):continue
   path,_,anchor=target.partition('#');dst=(file.parent/unquote(path)).resolve() if path else file.resolve()
   if not dst.is_relative_to(ROOT.resolve()):errors.append('Enlace fuera de la carpeta '+str(file.relative_to(ROOT))+' -> '+target);continue
   link_count+=1
   if not dst.exists():errors.append('Enlace ausente '+str(file.relative_to(ROOT))+' -> '+target)
   elif anchor:
    anchor_count+=1
    if anchor not in anchors.get(dst,set()):errors.append('Ancla ausente '+str(file.relative_to(ROOT))+' -> '+target)
 sources=read_json('datos/fuentes.json')
 for source in sources:
  if 'ruta' not in source:continue
  file=ROOT/source['ruta']
  if not file.exists():warnings.append('Original no disponible en esta copia '+source['id'])
  elif hashlib.sha256(file.read_bytes()).hexdigest()!=source['sha256']:errors.append('Huella alterada '+source['id'])
 messages=read_json('datos/mensajes.json');summary=read_json('datos/resumen.json')
 rows=collections.defaultdict(list)
 for m in messages:rows[m['entrevista']].append(m)
 if len(rows)!=summary['entrevistas_utilizables']:errors.append('Conteo de entrevistas inconsistente')
 if sum(m['emisor']=='Participante' for m in messages)!=summary['mensajes_participante']:errors.append('Conteo de respuestas inconsistente')
 for interview,ms in rows.items():
  orders=[m['orden'] for m in ms]
  if len(orders)!=len(set(orders)):errors.append('Órdenes duplicados '+interview)
  for m in ms:
   if 'm-'+str(m['orden']) not in anchors.get((ROOT/'raw/transcripciones'/f'{interview}.md').resolve(),set()):errors.append('Mensaje sin ancla '+interview)
 identity_file=ROOT/'raw/restringido/identidades.json'
 if identity_file.exists():
  identity=json.loads(identity_file.read_text());eids=[i['entrevista'] for i in identity]
  if len(eids)!=len(set(eids)):errors.append('Colisión de identificadores abreviados')
  for i in identity:
   if i['entrevista']!='E-'+i['id_original'][:8]:errors.append('Identificador inconsistente')
  # Direct email fields must not leak outside restricted data. Quotations can retain organizations.
  emails={i['email'].casefold() for i in identity if i['email']}
  for file in ROOT.rglob('*'):
   if not file.is_file() or 'restringido' in file.parts or file.suffix not in ('.md','.json','.csv','.py'):continue
   text=file.read_text(encoding='utf-8').casefold()
   for email in emails:
    if email in text:errors.append('Correo de identidad fuera de carpeta restringida '+str(file.relative_to(ROOT)));break
 by_message={(m['entrevista'],m['orden']):m for m in messages}
 def evidence_norm(text):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',text)).strip().casefold()
 for datafile in ('datos/codificaciones.json','datos/pni.json'):
  for row in read_json(datafile):
   for order in row['mensajes_csv']:
    m=by_message.get((row['entrevista'],order))
    if not m or m['emisor']!='Participante' or evidence_norm(row['fragmento']) not in evidence_norm(m['texto']):errors.append('Referencia de evidencia inconsistente '+datafile+' '+row['entrevista'])
 for file in (ROOT/'wiki').rglob('*.md'):
  for interview,order in re.findall(r'raw/transcripciones/(E-[0-9a-f]{8})\.md#m-(\d+)',file.read_text(encoding='utf-8')):
   m=by_message.get((interview,int(order)))
   if not m or m['emisor']!='Participante':errors.append('Cita de evidencia no apunta a participante '+str(file.relative_to(ROOT)))
 for dir_name,key_name in [('entrevistas','entrevistas_utilizables'),('temas','temas'),('conceptos','conceptos')]:
  count=summary[key_name]
  actual=len(list((ROOT/'wiki'/dir_name).glob('*.md')))
  if actual!=count:errors.append('Conteo no esperado '+dir_name+': '+str(actual))
 # Index every curated page, including maintenance reports.
 index=(ROOT/'index.md').read_text(encoding='utf-8')
 for file in (ROOT/'wiki').rglob('*.md'):
  if str(file.relative_to(ROOT)) not in index:errors.append('Página ausente del índice '+str(file.relative_to(ROOT)))
 result={'estado':'correcto' if not errors else 'errores','archivos_markdown':len(files),'enlaces_locales_verificados':link_count,'referencias_a_mensajes_verificadas':anchor_count,'errores':errors,'advertencias':warnings,'revision_semantica':'pendiente','resultados_externos':'no verificados'}
 print(json.dumps(result,ensure_ascii=False,indent=2))
 return result

def stage(csv_path):
 file=Path(csv_path).expanduser().resolve()
 if not file.is_file():raise ValueError('El archivo CSV no existe.')
 with file.open(encoding='utf-8-sig',newline='') as f:
  reader=csv.DictReader(f);required={'entrevista_id','estado','mensaje_orden','emisor','mensaje','mensaje_fecha'}
  if not required.issubset(reader.fieldnames or []):raise ValueError('CSV sin columnas requeridas '+', '.join(sorted(required-set(reader.fieldnames or []))))
  rows=list(reader)
 if not rows:raise ValueError('CSV sin mensajes.')
 new=collections.defaultdict(list);seen=set();state_by_id={}
 for r in rows:
  if not r['entrevista_id'] or not re.fullmatch(r'[0-9a-fA-F]{8}-[0-9a-fA-F-]{27}',r['entrevista_id']):raise ValueError('ID de entrevista inválido.')
  try:order=int(r['mensaje_orden'])
  except ValueError:raise ValueError('Orden de mensaje no entero.')
  if r['emisor'] not in ('IA','Participante'):raise ValueError('Emisor no reconocido.')
  item=(r['entrevista_id'],order)
  if item in seen:raise ValueError('ID y orden de mensaje duplicados.')
  seen.add(item)
  if r['entrevista_id'] in state_by_id and state_by_id[r['entrevista_id']]!=r['estado']:raise ValueError('Estado inconsistente dentro de una entrevista.')
  state_by_id[r['entrevista_id']]=r['estado'];new[r['entrevista_id']].append(r)
 sha=hashlib.sha256(file.read_bytes()).hexdigest();folder=ROOT/'.staging'/sha[:16]
 if folder.exists():
  print('Fuente ya preparada en '+str(folder.relative_to(ROOT)));return
 oldfile=ROOT/'raw/restringido/entrevistas-original.csv'
 if not oldfile.exists():raise ValueError('Falta el CSV original para comparar IDs completos. Prepare la copia privada completa.')
 with oldfile.open(encoding='utf-8-sig',newline='') as f:oldrows=list(csv.DictReader(f))
 old=collections.defaultdict(list)
 for r in oldrows:old[r['entrevista_id']].append(r)
 abbrev=collections.defaultdict(set)
 for k in set(new)|set(old):abbrev['E-'+k[:8]].add(k)
 if any(len(ids)>1 for ids in abbrev.values()):raise ValueError('Colisión de ID abreviado; requiere resolver el esquema antes del ingreso.')
 report=[]
 def content(ms):return [(int(r['mensaje_orden']),r['emisor'],r['mensaje']) for r in sorted(ms,key=lambda x:int(x['mensaje_orden']))]
 for k,ms in new.items():
  comparison='nueva' if k not in old else ('contenido_igual' if content(ms)==content(old[k]) else 'contenido_distinto')
  report.append({'uuid':k,'entrevista':'E-'+k[:8],'comparacion':comparison,'estado_nuevo':ms[0]['estado'],'estado_anterior':old[k][0]['estado'] if k in old else None,'mensajes_nuevos':len(ms),'mensajes_anteriores':len(old[k]) if k in old else None})
 folder.mkdir(parents=True)
 shutil.copyfile(file,folder/'fuente.csv')
 manifest={'fuente_nombre':file.name,'sha256':sha,'preparada_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'registros':len(new),'mensajes':len(rows),'comparacion':report,'estado':'pendiente de integración por agente','restriccion':'fuente con datos personales; no publicar'}
 (folder/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 (folder/'README.md').write_text('Fuente preparada. El agente debe leer AGENTS.md, revisar manifest.json y conciliar las versiones antes de crear páginas. Esta operación no actualiza la wiki ni sus métricas.\n',encoding='utf-8')
 print(json.dumps({'paquete':str(folder.relative_to(ROOT)),'registros':len(new),'mensajes':len(rows),'resumen':dict(collections.Counter(r['comparacion'] for r in report))},ensure_ascii=False,indent=2))

def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
 s=sub.add_parser('search');s.add_argument('query');s.add_argument('--limit',type=int,default=5)
 sub.add_parser('validate');sub.add_parser('status')
 s=sub.add_parser('stage');s.add_argument('csv_path')
 args=p.parse_args()
 try:
  if args.action=='search':search(args.query,max(1,min(args.limit,50)))
  elif args.action=='status':print(json.dumps(read_json('datos/resumen.json'),ensure_ascii=False,indent=2))
  elif args.action=='stage':stage(args.csv_path)
  else:sys.exit(0 if not validate()['errores'] else 1)
 except (ValueError,OSError,csv.Error,json.JSONDecodeError) as e:
  print('Error '+str(e),file=sys.stderr);sys.exit(2)

if __name__=='__main__':main()
