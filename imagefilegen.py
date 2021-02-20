
filename_base = "img_"
img_list_file = open('./img_list/test_img_list.txt', 'w')
for w in range (1,5):
    for v in range (1,5):
        filename = [filename_base + str(w) + "_" + str(v) + "_minus.png", " ", filename_base + str(w) + "_" + str(v) + "_normal.png", " ", filename_base + str(w) + "_" + str(v) + "_plus.png", " flow_" + str(w) + "_" + str(v) + "\n"]
        img_list_file.writelines(filename)
img_list_file.close()
