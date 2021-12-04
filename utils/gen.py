import os
import csv
import subprocess

data_filename = './../data/survey.csv'
source_folder = '/Users/julianeverett/DorkingTreesForLife/DruidsGrove/DruidsGrove-Survey/'
proj_folder = '/Users/julianeverett/Development/workspace/druids-grove-tree-survey/'

def main():
  with open(data_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0][:2] == 'DG':
        tree_id = row[0].lower()
        # create_images(tree_id)
        create_page(tree_id, row)

def create_images(tree_id):
  for filename in os.listdir(os.path.join(source_folder, tree_id)):
    img = os.path.join(source_folder, tree_id, filename)
    if os.path.isfile(img) and img.lower().endswith('.jpg') and not img.lower().endswith('_x.jpg'):
      if not os.path.isdir(os.path.join(proj_folder, tree_id)):
        os.mkdir(os.path.join(proj_folder, tree_id))
      out_w = os.path.join(proj_folder, 'images', tree_id, filename[0:-4]+'_w.jpg')
      command = [
        'magick',
        img,
        '-resize',
        '40%',
        '-define',
        'filter:lobes=4',
        '-filter',
        'Lanczos',
        out_w
      ]
      subprocess.run(command)
      out_th = os.path.join(proj_folder, 'images', tree_id, filename[0:-4]+'_th.jpg')
      command = [
        'magick',
        out_w,
        '-resize',
        '40%',
        '-define',
        'filter:lobes=4',
        '-filter',
        'Lanczos',
        out_th
      ]
      subprocess.run(command)

def create_page(tree_id, row):
  with open('gen.tpl') as f:
    page = f.read()
  gallery = ''
  for img in os.listdir(os.path.join(proj_folder, 'images', tree_id)):
    if not img.endswith('_th.jpg'):
      filename = img[0:-6]
      if 'canopy' in filename:
        canopy_img = filename
      elif 'litter' in filename:
        leaf_litter_img = filename
      else:
        gallery = gallery + create_img(tree_id, filename)
  page = page.replace('{{id}}', tree_id)
  page = page.replace('{{canopy_img}}', canopy_img)
  page = page.replace('{{leaf_litter_img}}', leaf_litter_img)
  page = page.replace('{{gallery}}', gallery)
  page = page.replace('{{latlong}}', row[2])
  page = page.replace('{{osgl}}', row[1])
  page = page.replace('{{2012osgl}}', row[3])
  page = page.replace('{{sex}}', row[4])
  page = page.replace('{{canopy}}', row[5])
  page = page.replace('{{leaf_litter}}', row[6])
  page = page.replace('{{girth_ft}}', row[7])
  page = page.replace('{{girth_m}}', row[8])
  page = page.replace('{{height}}', row[9])
  page = page.replace('{{comments}}', row[10])
  with open(os.path.join(proj_folder, 'pages', tree_id+'.md'), 'w') as f:
     f.write(page)

def create_img(tree_id, filename):
  img = '  - url: ./images/'+tree_id+'/'+filename+'_w.jpg\n'
  img = img + '    image_path: ./images/'+tree_id+'/'+filename+'_th.jpg\n'
  img = img + '    alt: "Tree Ref '+tree_id+'"\n'
  img = img + '    title: "Tree Ref '+tree_id+'"\n'
  return img



main()
print('done.')