#author = "Lee Hir"
import os
pic_path = 'F:\\pic\\pictures\\new_scheme\\VOCdevkit\\VOC2007\\JPEGImages\\'
xml_path = 'F:\\pic\\pictures\\new_scheme\\VOCdevkit\\VOC2007\\Annotations\\'
def delet_xml(xml_path,pic_path):
    xml_l = os.listdir(xml_path)
    pic_l = os.listdir(pic_path)
    xml_list = [x.split('.')[0] for x in xml_l]
    pic_list = [x.split('.')[0] for x in pic_l]
    for a in xml_list:
        if a not in pic_list:
            os.remove(xml_path + a + '.xml')

if __name__ == '__main__':
    delet_xml(xml_path,pic_path)