Name:           ros-indigo-evapc-ros
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS evapc_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/evapc_ros
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-evarobot-description
Requires:       ros-indigo-evarobot-navigation
Requires:       ros-indigo-evarobot-pose-ekf
Requires:       ros-indigo-evarobot-slam
Requires:       ros-indigo-evarobot-state-publisher
Requires:       ros-indigo-impc-msgs
BuildRequires:  ros-indigo-catkin

%description
The evapc_ros meta package provides all the basic packages for Gazebo model and
navigation of Evarobot.

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

