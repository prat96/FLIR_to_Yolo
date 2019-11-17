import glob, os

os.chdir("/home/triton/code/darknet/flir/images/val/")
for file in glob.glob("*.jpeg"):
    label = "/home/triton/code/darknet/flir/images/val/" + file + '\n'
    print(label)
    file = open('../' + 'val_flir_images' + '.txt', 'a')
    file.write(label)
    file.close()
