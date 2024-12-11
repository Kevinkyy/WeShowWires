from arena import *
from datetime import datetime

scene = Scene(host="arena-dev1.conix.io", scene="CICKitchen")

node_count = 0
cam_obj = None

# Previous function to add a card
def Good_ClickHandler(scene, evt, msg):
    # if evt.type == "mousedown" or evt.type == "touchstart":
    global node_count
    node_title = "Maintenance Check " + str(node_count)
    node_count += 1
    curr_time = datetime.now().strftime("%m-%d-%Y %H:%M")
    node_body = "Created at " + curr_time + "\n" + "Everything is good!"
    node = Card(
        object_id="node_" + str(node_count),
        persist=False,
        clickable=True,
        title=node_title,
        body=node_body,
        bodyAlign="center",
        position=(cam_obj.data.position.x, cam_obj.data.position.y, cam_obj.data.position.z),
        widthScale=0.75,
        look_at="#my-camera",
        img="store/users/zhizhouh/scenes/CICKitchen/good.png",
        scale=(0.25, 0.25, 0.25)
    )
    scene.add_object(node)
    print("Good Card added!")

def Attention_ClickHandler(scene, evt, msg):
    # if evt.type == "mousedown" or evt.type == "touchstart":
    global node_count
    node_title = "Maintenance Check " + str(node_count)
    node_count += 1
    curr_time = datetime.now().strftime("%m-%d-%Y %H:%M")
    node_body = "Created at " + curr_time + "\n" + "Attention! Need maintence soon!"
    node = Card(
        object_id="node_" + str(node_count),
        persist=False,
        clickable=True,
        title=node_title,
        body=node_body,
        bodyAlign="center",
        position=(cam_obj.data.position.x, cam_obj.data.position.y, cam_obj.data.position.z),
        widthScale=0.75,
        look_at="#my-camera",
        img="store/users/zhizhouh/scenes/CICKitchen/attention.jpg",
        scale=(0.25, 0.25, 0.25)
    )
    scene.add_object(node)
    print("Attention Card added!")

def Severe_ClickHandler(scene, evt, msg):
    # if evt.type == "mousedown" or evt.type == "touchstart":
    global node_count
    node_title = "Maintenance Check " + str(node_count)
    node_count += 1
    curr_time = datetime.now().strftime("%m-%d-%Y %H:%M")
    node_body = "Created at " + curr_time + "\n" + "Warning! Wire in severe condition, need to replace now!"
    node = Card(
        object_id="node_" + str(node_count),
        persist=False,
        clickable=True,
        title=node_title,
        body=node_body,
        bodyAlign="center",
        position=(cam_obj.data.position.x, cam_obj.data.position.y, cam_obj.data.position.z),
        widthScale=0.75,
        look_at="#my-camera",
        img="store/users/zhizhouh/scenes/CICKitchen/severe.png",
        scale=(0.25, 0.25, 0.25)
    )
    scene.add_object(node)
    print("Severe Card added!")

# def user_join_callback(scene, cam, msg):
#     print("User joined:", cam.object_id)
#     global cam_obj
#     cam_obj = cam
#     circle1 = Circle(
#         parent=cam.object_id,
#         position=(0, -0.05, -0.35),
#         scale=(0.01, 0.01, 0.01),
#         color=(0, 255, 0), # green
#         clickable=True,
#         title="Add Node",
#         evt_handler=Good_ClickHandler
#     )
#     scene.add_object(circle1)
#     circle2 = Circle(
#         parent=cam.object_id,
#         position=(-0.1, -0.05, -0.35),
#         scale=(0.01, 0.01, 0.01),
#         color=(255, 255, 0), # yellow
#         clickable=True,
#         title="Add Node",
#         evt_handler=Attention_ClickHandler
#     )
#     scene.add_object(circle2)
#     circle3 = Circle(
#         parent=cam.object_id,
#         position=(0.1, -0.05, -0.35),
#         scale=(0.01, 0.01, 0.01),
#         color=(255, 0, 0), # red
#         clickable=True,
#         title="Add Node",
#         evt_handler=Severe_ClickHandler
#     )
#     scene.add_object(circle3)
#     print("Circle added for card creation.")

# scene.user_join_callback = user_join_callback

def user_join_callback(scene, cam, msg):
    print("User joined:", cam.object_id)
    global cam_obj
    cam_obj = cam
    
    def button_handler(_scene, evt, _msg):
        if evt.type == "buttonClick":
            if evt.data.buttonName == "Good!":
                print("Green Button clicked!")
                # Call Good_ClickHandler logic
                Good_ClickHandler(_scene, evt, _msg)
            elif evt.data.buttonName == "Warning!":
                print("Yellow Button clicked!")
                # Call Attention_ClickHandler logic
                Attention_ClickHandler(_scene, evt, _msg)
            elif evt.data.buttonName == "Severe!":
                print("Red Button clicked!")
                # Call Severe_ClickHandler logic
                Severe_ClickHandler(_scene, evt, _msg)

    button_set = [
        Button(name="Good!", color=(0, 255, 0)),  # Green button
        Button(name="Warning!", color=(255, 255, 0)),  # Yellow button
        Button(name="Severe!", color=(255, 0, 0)),  # Red button
    ]

    button_panel = ButtonPanel(
        object_id="button-panel",
        parent=cam.object_id,
        persist=False,
        title="Condition?",
        buttons=button_set,
        vertical=False,
        font="Roboto-Mono",
        position=(0, -0.05, -0.35),
        scale=(0.1, 0.1, 0.1),
        evt_handler=button_handler,
    )
    
    scene.add_object(button_panel)
    print("Button panel added.")

scene.user_join_callback = user_join_callback

# New functionality to toggle wire visibility
# Wire segments
kitchen_wire = GLTF(
    object_id="Kitchen",
    position=(6, 0.5, 10.2), 
    rotation=(-180, 0, -180),
    scale=(1, 1, 1),
    url="store/users/zhizhouh/scenes/CICKitchen/Kitchen.glb"
)

outlet_wire = GLTF(
    object_id="Outlet",
    position=(6, 0.5, 10.2), 
    rotation=(-180, 0, -180),
    scale=(1, 1, 1),
    url="store/users/zhizhouh/scenes/CICKitchen/Outlet.glb"
)

tv_cable_wire = GLTF(
    object_id="TV_cable",
    position=(6, 0.5, 10.2), 
    rotation=(-180, 0, -180),
    scale=(1, 1, 1),
    url="store/users/zhizhouh/scenes/CICKitchen/TV.glb"
)

refrigerator_wire = GLTF(
    object_id="refrigerator",
    position=(6, 0.5, 10.2), 
    rotation=(-180, 0, -180),
    scale=(1, 1, 1),
    url="store/users/zhizhouh/scenes/CICKitchen/Refrigerator.glb"
)




# Invisible boxes for click
def kitchen_ClickHandler(scene, evt, msg):
    if evt.type == "mousedown" or evt.type == "touchstart":
        print("kitchen clicked")
        kitchen_wire.data.visible = not kitchen_wire.data.visible
        scene.update_object(kitchen_wire)

kitchen_box = Box(
    object_id="kitchen_box1",
    persist=False,
    position=(3.5, 0.5, 0), 
    depth=1.5,
    height=2.5,
    width=4,
    # color=(0, 0, 0),
    # opacity=0,
    clickable=True,
    visible=False,
    evt_handler = kitchen_ClickHandler
)

def outlet_ClickHandler(scene, evt, msg):
    if evt.type == "mousedown" or evt.type == "touchstart":
        print("outlet clicked")
        outlet_wire.data.visible = not outlet_wire.data.visible
        scene.update_object(outlet_wire)

outlet_box = Box(
    object_id="outlet_box1",
    persist=False,
    position=(3.2, 2, -5.6), 
    depth=1,
    height=3,
    width=1.5,
    # color=(0, 0, 0),
    clickable=True,
    visible=False,
    # opacity=0,
    evt_handler = outlet_ClickHandler
)

def TV_ClickHandler(scene, evt, msg):
    if evt.type == "mousedown" or evt.type == "touchstart":
        print("TV clicked")
        tv_cable_wire.data.visible = not tv_cable_wire.data.visible
        scene.update_object(tv_cable_wire)

tv_cable_box = Box(
    object_id="tv_cable_box1",
    persist=False,
    position=(-0.5, 1.5, -4.5), 
    depth=3,
    height=2,
    width=0.5,
    # color=(0, 0, 0),
    clickable=True,
    visible=False,
    # opacity=0,
    evt_handler = TV_ClickHandler

)

def Ref_ClickHandler(scene, evt, msg):
    if evt.type == "mousedown" or evt.type == "touchstart":
        print("Refrigerator clicked")
        refrigerator_wire.data.visible = not refrigerator_wire.data.visible
        scene.update_object(refrigerator_wire)


refrigerator_box = Box(
    object_id="refrigerator_box1",
    persist=False,
    position=(5, 1, -3.3), 
    depth=1,
    height=2.1,
    width=1.5,
    # color=(0, 0, 0),
    clickable=True,
    visible=False,
    # opacity=0,
    evt_handler = Ref_ClickHandler
)

@scene.run_once
def init():
    refrigerator_box.data.visible = False
    tv_cable_box.data.visible = False
    outlet_box.data.visible = False
    kitchen_box.data.visible = False
    refrigerator_wire.data.visible = False
    tv_cable_wire.data.visible = False
    outlet_wire.data.visible = False
    kitchen_wire.data.visible = False
    # Add boxes to the scene
    scene.add_object(kitchen_box)
    scene.add_object(outlet_box)
    scene.add_object(tv_cable_box)
    scene.add_object(refrigerator_box)
    scene.add_object(kitchen_wire)
    print("Kitchen wire added.")
    scene.add_object(outlet_wire)
    print("Outlet wire added.")
    scene.add_object(tv_cable_wire)
    print("TV cable wire added.")
    scene.add_object(refrigerator_wire)
    print("Refrigerator wire added.")

# Run tasks
scene.run_tasks()