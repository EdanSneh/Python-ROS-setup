cmake_minimum_required(VERSION 2.8)
project(my_pkg)

find_package(catkin REQUIRED COMPONENTS
    roscpp

)
find_package(Boost REQUIRED COMPONENTS thread system)

catkin_python_setup()

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS roscpp
)

add_executable(my_node_cpp src/my_node_npp.cpp)
target_link_libraries(my_node_cpp ${PROJECT_NAME})

