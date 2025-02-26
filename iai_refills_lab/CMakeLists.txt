cmake_minimum_required(VERSION 3.5)
project(iai_refills_lab)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(DIRECTORY maps urdf
  DESTINATION share/${PROJECT_NAME})

install(PROGRAMS script/pixel_coordinates_to_m.py
    DESTINATION lib/${PROJECT_NAME})

ament_package()