import depthai as dai


def tag_billede():
    with dai.Pipeline() as pipeline:
        cam = pipeline.create(dai.node.Camera).build()
        V = cam.requestOutput((1280, 720)).createOutputQueue()
        pipeline.start()
        for _ in range(120):
            img = V.get().getCvFrame()
    return img