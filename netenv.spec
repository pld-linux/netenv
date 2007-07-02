
%define		_mainver	0.94-3
%define		_ver	%(echo %{_mainver} |tr - .)

Summary:	Netenv
Summary(pl.UTF-8):	Netenv
Name:		netenv
Version:	%{_ver}
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://netenv.sourceforge.net/%{name}-%{_mainver}.tar.gz
# Source0-md5:	0ce0f5042bbe01c80171ab4085809f97
Patch0:		%{name}-Makefile.patch
URL:		http://netenv.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When booting your laptop netenv provides you with a simple interface
from which you can choose the current network environment. If you are
the first time in an environment, you can enter the basic data for
later reuse.

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}-%{_mainver}
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{_bindir}/trpnc
%attr(755,root,root) %{_sbindir}/netenv
