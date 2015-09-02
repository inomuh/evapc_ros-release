Name:           ros-indigo-evarobot-description
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS evarobot_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/evarobot_description
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-indigo-angles
Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-driver-base
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-gazebo-msgs
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-hector-gazebo-plugins
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-impc-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-polled-camera
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-urdf
BuildRequires:  gazebo-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-driver-base
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-gazebo-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-hector-gazebo-plugins
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-impc-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-polled-camera
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rosgraph-msgs
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf2-ros
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-urdf

%description
evarobot_description provides a complete 3D model of the Evarobot for simulation
and visualization.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Sep 03 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Fri Aug 28 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

