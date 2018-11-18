cmake_minimum_required(VERSION 2.8.3)
project(voice_commander)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)


catkin_package(

  CATKIN_DEPENDS roscpp std_msgs message_runtime
  
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(${PROJECT_NAME}_node src/voice_commander_node.cpp)


target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
add_dependencies(${PROJECT_NAME}_node ${PROJECT_NAME}_generate_messages_cpp)

