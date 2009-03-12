Name:			oggconvert
Version:		0.3.2
Release:		%mkrel 1
Summary:		A small utility for converting media files into Ogg, Theora and Dirac formats
Group:			Sound
License:		LGPLv2
Source:			http://oggconvert.tristanb.net/releases/%version/%name-%version.tar.gz
URL:			http://oggconvert.tristanb.net/
BuildArch:		noarch
BuildRoot:		%_tmppath/%name-%version-%release-buildroot
BuildRequires:		python-devel gstreamer0.10-python desktop-file-utils
%if %mdkversion < 200900
Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils
%endif
Requires:		python-gtk python-gtk-glade gstreamer0.10-python
Requires:		gstreamer0.10-plugins-base
Suggests:		gstreamer0.10-plugins-good
Suggests:		gstreamer0.10-plugins-bad
Suggests:		gstreamer0.10-plugins-ugly
suggests:		gstreamer0.10-schroedinger

%description
OggConvert is a small, open source utility for converting audio and video files 
into the Vorbis audio format, and the Theora and Dirac video formats.

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%update_menus
%clean_desktop_database
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/%name
%python_sitelib/*.egg-info
%python_sitelib/OggConvert
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.svg

#-------------------------------------------------------------------------------

%prep
%setup -q

# fix perm on doc files
chmod 644 AUTHORS COPYING ChangeLog README TODO

%build
%__python setup.py build

%install
rm -rf %buildroot
%__python setup.py install --root %buildroot 

desktop-file-install \
  --add-category="GTK" \
  --add-category="Audio" \
  --remove-key="GenericName[en_GB]" \
  --dir %buildroot%_datadir/applications %buildroot%_datadir/applications/*

%find_lang %name

%clean
rm -rf %buildroot

