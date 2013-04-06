#!/usr/bin/env python
import rospy
import random
from cafe_msgs.msg import OrderList, Order, Menu

MENU_NAME = ["Cafe Latte", "Capuccino", "DDal Ba", "Coke", "Americano", "Koreano", "Kobukino", "Sul tang mool"]
ROBOT_NAME = ["Kobuki", "Guimul", "KobukKobuk","Snail","Jola Bbareun Kobuki","Motorized Kobuki"]

def generateMenus():
    
    menus = []

    for i in range(1,4):
        m = Menu()
        m.name = random.choice(MENU_NAME)
        m.size = random.randint(1,3)
        m.qty = random.randint(1,500)
        menus.append(m)

    return menus 

def generateFakeOrder(order_num):
    o = Order()
    o.table_id = random.randint(0,10)
    o.menus = generateMenus()
    o.robot_name = random.choice(ROBOT_NAME)
    o.order_id = order_num
    return o

def pubOrderList():
    pub = rospy.Publisher('fake_orderlist',OrderList,latch = True)

    num_order = 1
    rospy.loginfo("Initialized..")
    while not rospy.is_shutdown():
        order_list = OrderList()
        order_list.orders = []

        list_num = random.randint(1,5)
        for i in range(list_num):
            order = generateFakeOrder(num_order)
            num_order = num_order + 1
            order_list.orders.append(order)

        rospy.loginfo("Publishing New Order List...")
        pub.publish(order_list)
        rospy.sleep(10)
        


if __name__ == "__main__":
    try:
        rospy.init_node('fake_orderlist_pub')
        pubOrderList()
    except rospy.ROSInterruptException: pass