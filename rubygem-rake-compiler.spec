%define oname rake-compiler

Name:       rubygem-%{oname}
Version:    0.7.5
Release:    %mkrel 1
Summary:    Rake-based Ruby Extension (C, Java) task generator
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/luislavena/rake-compiler
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Provide a standard and simplified way to build and package
Ruby extensions (C, Java) using Rake as glue.


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib -type f -exec sed -i -e '/#!/d' {} \;

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/rake-compiler
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/Isolate
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/tasks/
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
