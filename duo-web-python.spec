%define name duo-web-python
%define version 1.1
%define unmangled_version 1.1
%define release 1

Summary: Duo Web SDK for two-factor authentication
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Duo Security, Inc. <support@duosecurity.com>
Url: https://github.com/duosecurity/duo_python

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%config(noreplace) /etc/httpd/conf.d/duo-js.conf
%config(noreplace) /etc/duo/duo_web.conf
%dir %{_datadir}/javascript/duo
%{_datadir}/javascript/duo/*
%dir %{python_sitelib}/duo_web
%{python_sitelib}/duo_web/*
%{python_sitelib}/*egg-info
%defattr(-,root,root)
