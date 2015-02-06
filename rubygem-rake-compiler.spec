%define oname rake-compiler

Name:       rubygem-%{oname}
Version:    0.8.0
Release:	3
Summary:    Rake-based Ruby Extension (C, Java) task generator
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/luislavena/rake-compiler
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
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
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib -type f -exec sed -i -e '/#!/d' {} \;

%files
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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Jan 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.0-1
+ Revision: 769363
- version update 0.8.0

* Sat Dec 18 2010 Rémy Clouard <shikamaru@mandriva.org> 0.7.5-1mdv2011.0
+ Revision: 622891
- Bump release
- new version 0.7.5
- remove ugly hack now that dependencies are fixed

* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 0.7.1-2mdv2011.0
+ Revision: 609237
- FIXME: make rubygem-rake-compiler installable
  The problem is that development dependencies include cucumber
  in version >= 0.4.4 and < 0.5 while we have 0.9.4
  and rspec >= 1.2.9 and < 1.3.0 while we have 2.0.1
  These are development dependencies so I assume it should work without it
  but a cleaner way would be to make it compatible with the versions we have
  but I didn?\226?\128?\153t have time to dig into it to see what would change.

* Thu Nov 04 2010 Rémy Clouard <shikamaru@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 593483
- import rubygem-rake-compiler

