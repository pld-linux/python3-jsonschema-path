Summary:	JSONSchema Spec with object-oriented paths
Summary(pl.UTF-8):	Specyfikacja JSONSchema ze ścieżkami zorientowanymi obiektowo
Name:		python3-jsonschema-path
Version:	0.5.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jsonschema-path/
Source0:	https://files.pythonhosted.org/packages/source/j/jsonschema-path/jsonschema_path-%{version}.tar.gz
# Source0-md5:	7837c15f78765ea256ab44cce039d36a
URL:		https://pypi.org/project/jsonschema-path/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented JSONSchema. Key features:
- Traverse schema like paths
- Access schema on demand with separate dereferencing accessor layer

%description -l pl.UTF-8
JSONSchema zorientowany obiektowo. Główne możliwości:
- przechodzenie schematu jak ścieżek
- dostęp do schematu na żądanie z osobną warstwą dostępu

%prep
%setup -q -n jsonschema_path-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/jsonschema_path
%{py3_sitescriptdir}/jsonschema_path-%{version}.dist-info
