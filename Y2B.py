#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@author: Dongyu Zhang
"""
from absl import app, flags
import re
import os
import requests
from xml.dom import minidom
import time

flags.DEFINE_string('youtube_url', None, 'Youtube video url, example: https://www.youtube.com/watch?v=mhIeiUbH2gg')
flags.DEFINE_string('dir', None, 'Output File Directories, example: H:\MyDanmakuFiles')
flags.DEFINE_string('name', None, 'output file Names, example: mydanmaku')
flags.mark_flag_as_required('youtube_url')

FLAGS = flags.FLAGS


def main(argv):
    del argv
    url = FLAGS.youtube_url
    out_dir = FLAGS.dir
    filename = FLAGS.name
    y2b(youtube_url=url, out_dir=out_dir, filename=filename)


def y2b(youtube_url, out_dir=None, filename=None):
    assert re.search("www.youtube.com/watch\?v=", youtube_url) is not None, "It is not a youtube video link"
    video_id = youtube_url.split("v=")[1]
    url = "https://serene-hollows-62567.herokuapp.com/api/v3/comments/"+video_id
    try:
        jpage = requests.get(url)
    except:
        print("Connection Failed")
    else:
        jfile = jpage.json()
        assert len(jfile['data']['comments'])>=1, "No comment available"
        doc = minidom.Document()
        root = doc.createElement('i')
        doc.appendChild(root)
        new_max_limit = str(len(jfile['data']['comments']))
        elelist = [('chatserver', 'chat.bilibili.com'), ('chatid', video_id),
                   ('mission', '0'), ('maxlimit', new_max_limit),
                   ('state', '0'), ('real_name', '0'), ('source', 'k-v')]
        for ele in elelist:
            new_e = doc.createElement(ele[0])
            new_e.appendChild(doc.createTextNode(ele[1]))
            root.appendChild(new_e)
        for i in jfile['data']['comments']:
            p_list = []
            stime = "%.5f"%(float(i['stime'])/1000.0)
            p_list.append(stime)
            p_list.append(str(i['mode']))
            p_list.append('25')
            p_list.append(str(i['color']))
            p_list.append(str(int(time.time())))
            p_list.append("0")
            p_list.append(str(i['user_id']))
            p_list.append(str(i['comment_id']))
            new_d = doc.createElement('d')
            new_d.setAttribute('p', ','.join(p_list))
            new_d.appendChild(doc.createTextNode(i['text']))
            root.appendChild(new_d)
        if out_dir is None:
            if filename is None:
                output_file = video_id+'.xml'
            else:
                output_file = filename+'.xml'
        else:
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)
            if filename is None:
                output_file = video_id + '.xml'
                output_file = os.path.join(out_dir, output_file)
            else:
                output_file = filename + '.xml'
                output_file = os.path.join(out_dir, output_file)
        with open(output_file, 'w', encoding="utf-8") as fp:
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
        print("Finished, the output file is %s" % output_file)


if __name__ == "__main__":
    app.run(main)
