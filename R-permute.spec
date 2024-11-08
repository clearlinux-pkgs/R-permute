#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-permute
Version  : 0.9.7
Release  : 50
URL      : https://cran.r-project.org/src/contrib/permute_0.9-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/permute_0.9-7.tar.gz
Summary  : Functions for Generating Restricted Permutations of Data
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
## Restricted permutations with R
[![CRAN version](http://www.r-pkg.org/badges/version/permute)](https://cran.r-project.org/package=permute)
[![](http://cranlogs.r-pkg.org/badges/grand-total/permute)](https://cran.r-project.org/package=permute)
[![R-CMD-check](https://github.com/gavinsimpson/permute/workflows/R-CMD-check/badge.svg)](https://github.com/gavinsimpson/cocorresp/actions)
[![codecov.io](https://codecov.io/github/gavinsimpson/permute/coverage.svg?branch=master)](https://codecov.io/github/gavinsimpson/permute?branch=master)

%prep
%setup -q -c -n permute
cd %{_builddir}/permute

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643306041

%install
export SOURCE_DATE_EPOCH=1643306041
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc permute || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/permute/COPYRIGHTS
/usr/lib64/R/library/permute/ChangeLog
/usr/lib64/R/library/permute/DESCRIPTION
/usr/lib64/R/library/permute/INDEX
/usr/lib64/R/library/permute/Meta/Rd.rds
/usr/lib64/R/library/permute/Meta/data.rds
/usr/lib64/R/library/permute/Meta/features.rds
/usr/lib64/R/library/permute/Meta/hsearch.rds
/usr/lib64/R/library/permute/Meta/links.rds
/usr/lib64/R/library/permute/Meta/nsInfo.rds
/usr/lib64/R/library/permute/Meta/package.rds
/usr/lib64/R/library/permute/Meta/vignette.rds
/usr/lib64/R/library/permute/NAMESPACE
/usr/lib64/R/library/permute/NEWS
/usr/lib64/R/library/permute/R/permute
/usr/lib64/R/library/permute/R/permute.rdb
/usr/lib64/R/library/permute/R/permute.rdx
/usr/lib64/R/library/permute/TODO.md
/usr/lib64/R/library/permute/data/jackal.rda
/usr/lib64/R/library/permute/doc/index.html
/usr/lib64/R/library/permute/doc/permutations.R
/usr/lib64/R/library/permute/doc/permutations.Rmd
/usr/lib64/R/library/permute/doc/permutations.html
/usr/lib64/R/library/permute/help/AnIndex
/usr/lib64/R/library/permute/help/aliases.rds
/usr/lib64/R/library/permute/help/paths.rds
/usr/lib64/R/library/permute/help/permute.rdb
/usr/lib64/R/library/permute/help/permute.rdx
/usr/lib64/R/library/permute/html/00Index.html
/usr/lib64/R/library/permute/html/R.css
/usr/lib64/R/library/permute/tests/Examples/permute-Ex.Rout.save
/usr/lib64/R/library/permute/tests/testthat.R
/usr/lib64/R/library/permute/tests/testthat/test-allPerms.R
/usr/lib64/R/library/permute/tests/testthat/test-as-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-blocks.R
/usr/lib64/R/library/permute/tests/testthat/test-check.R
/usr/lib64/R/library/permute/tests/testthat/test-get-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-how.R
/usr/lib64/R/library/permute/tests/testthat/test-nobs.R
/usr/lib64/R/library/permute/tests/testthat/test-numPerms.R
/usr/lib64/R/library/permute/tests/testthat/test-permute-fun.R
/usr/lib64/R/library/permute/tests/testthat/test-set-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffle-utils.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffle.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffleSet.R
