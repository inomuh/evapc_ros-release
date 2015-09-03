Name:           ros-indigo-evarobot-navigation
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS evarobot_navigation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/evarobot_navigation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-move-base
Requires:       ros-indigo-roscpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-move-base
BuildRequires:  ros-indigo-roscpp

%description
evarobot_navigation provides roslaunch script files to navigate the Evarobot.

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
* Thu Sep 03 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Thu Sep 03 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Fri Aug 28 2015 Mehmet Akcakoca <akcakocamehmet@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

