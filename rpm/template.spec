Name:           ros-jade-romeo-gazebo-plugin
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS romeo_gazebo_plugin package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-gazebo-plugins
Requires:       ros-jade-gazebo-ros
Requires:       ros-jade-gazebo-ros-control
Requires:       ros-jade-romeo-control
Requires:       ros-jade-romeo-description
Requires:       ros-jade-ros-control
Requires:       ros-jade-ros-controllers
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-gazebo-ros
BuildRequires:  ros-jade-romeo-description

%description
The romeo_gazebo_plugin package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Sep 20 2016 Natalia Lyubova <natalia.lyubova@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

