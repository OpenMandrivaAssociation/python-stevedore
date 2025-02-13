Name:		python-stevedore
Version:	5.4.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
Summary:	Manage dynamic plugins for Python applications
URL:		https://pypi.org/project/stevedore/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Manage dynamic plugins for Python applications

%files
%{py_sitedir}/stevedore
%{py_sitedir}/stevedore-*.*-info
