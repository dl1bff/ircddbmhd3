#
#
# ircddbmhd3
#
# Copyright (C) 2017   Michael Dirska, DL1BFF (dl1bff@mdx.de)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#



Name: ircddbmhd3
Version: 1.0
Release: 2
License: GPLv2
Group: Networking/Daemons
Summary: ircDDB mheard daemon
URL: http://ircddb.net
Packager: Michael Dirska DL1BFF <dl1bff@mdx.de>
Requires: libpcap >= 0.9, libconfig
%{?systemd_requires}
Source0: ircddbmhd3.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libpcap-devel, libconfig-devel, systemd



%description
The ircDDB-mheard daemon captures IP packets from an RP2C
DSTAR controller and sends its findings to a local UDP port.


%prep
%setup -n ircddbmhd3
echo "#define IRCDDBMHD_VERSION \"rpm:%{name}-%{version}-%{release}\"" > ircddbmhd_version.h



%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
cp %{name} %{buildroot}/%{_sbindir}/%{name}
mkdir -p %{buildroot}/etc
cp %{name}.conf %{buildroot}/etc/
mkdir -p %{buildroot}/%_unitdir
cp %{name}.service %{buildroot}/%_unitdir/%{name}.service
mkdir -p %{buildroot}/%_presetdir
cp %{name}.preset %{buildroot}/%_presetdir/51-%{name}.preset



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%config /etc/%{name}.conf
%attr(755,root,root) %{_sbindir}/%{name}
%_unitdir/%{name}.service
%_presetdir/51-%{name}.preset
%doc README.md COPYING LICENSE



%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service



