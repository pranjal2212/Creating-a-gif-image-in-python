import imageio
fn = ["C:\\img1.jpg","C:\\img2.jpg","C:\\img3.jpg","C:\\img4.jpg"]
images = []
for f in fn:
    images.append(imageio.imread(f))
imageio.mimsave('C:\\final.gif', images)
