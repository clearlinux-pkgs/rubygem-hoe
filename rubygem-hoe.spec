#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe
Version  : 3.13.1
Release  : 9
URL      : https://rubygems.org/downloads/hoe-3.13.1.gem
Source0  : https://rubygems.org/downloads/hoe-3.13.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-hoe-bin
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= Hoe
home  :: http://www.zenspider.com/projects/hoe.html
code  :: https://github.com/seattlerb/hoe
bugs  :: https://github.com/seattlerb/hoe/issues
rdoc  :: http://docs.seattlerb.org/hoe/
doco  :: http://docs.seattlerb.org/hoe/Hoe.pdf
other :: http://github.com/jbarnette/hoe-plugin-examples

%package bin
Summary: bin components for the rubygem-hoe package.
Group: Binaries

%description bin
bin components for the rubygem-hoe package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-3.13.1
gem spec %{SOURCE0} -l --ruby > rubygem-hoe.gemspec

%build
gem build rubygem-hoe.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-3.13.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
pushd %{buildroot}%{gem_dir}/gems/hoe-3.13.1
rake --trace test TESTOPTS="-v"
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/hoe-3.13.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/File/cdesc-File.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/File/read_utf-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Gem/cdesc-Gem.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Clean/cdesc-Clean.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Clean/clean_globs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Clean/define_clean_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Clean/initialize_clean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Compiler/activate_compiler_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Compiler/cdesc-Compiler.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Compiler/compile_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Compiler/define_compiler_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Compiler/initialize_compiler-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Debug/cdesc-Debug.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Debug/check_manifest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Debug/define_debug_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/cdesc-Deps.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/define_deps_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/dependent_upon-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/get_gems_by_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/get_latest_gems-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/get_source_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Deps/install_missing_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flay/cdesc-Flay.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flay/define_flay_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flay/flay_threshold-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flay/initialize_flay-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flog/cdesc-Flog.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flog/define_flog_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flog/flog_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flog/flog_threshold-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Flog/initialize_flog-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/GemPreludeSucks/cdesc-GemPreludeSucks.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Gemcutter/cdesc-Gemcutter.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Gemcutter/define_gemcutter_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Inline/activate_inline_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Inline/cdesc-Inline.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Inline/define_inline_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Newb/cdesc-Newb.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Newb/define_newb_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/cdesc-Package.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/define_package_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/initialize_package-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/install_gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/need_tar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/need_zip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Package/pkg_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/activate_publish_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/blog_categories-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/cdesc-Publish.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/define_publish_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/initialize_publish-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/local_rdoc_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/need_rdoc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/rdoc_locations-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/remote_rdoc_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Publish/rsync_args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/RCov/activate_rcov_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/RCov/cdesc-RCov.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/RCov/define_rcov_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/activate_racc_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/cdesc-Racc.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/define_racc_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/initialize_racc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/oedipus_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/racc_flags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Racc/racc_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Rake/cdesc-Rake.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Rdoc/cdesc-Rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Rdoc/define_rdoc_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Rdoc/initialize_rdoc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Signing/cdesc-Signing.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Signing/define_signing_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/define_test_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/initialize_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/make_test_cmd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/multiruby_skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/rspec_dirs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/rspec_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/test_prelude-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/testlib-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/try_loading_rspec1-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/Test/try_loading_rspec2-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/activate_plugin_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/activate_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/add_dependencies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/add_include_dirs-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/author-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/bad_plugins-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/cdesc-Hoe.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/define_spec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/dependency-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/dependency_target-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/description-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/description_sections-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/developer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/email-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/extra_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/extra_dev_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/extra_rdoc_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/group_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/have_gem%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/history_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/initialize_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/intuit_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/license-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/licenses-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/load_plugin_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/load_plugins-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/normalize_deps-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/paragraphs_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/parse_urls-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/pluggable%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/plugin%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/plugin-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/plugins-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/post_initialize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/post_install_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/read_manifest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/readme_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/require_ruby_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/require_rubygems_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/spec-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/spec_extras-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/summary-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/summary_sentences-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/test_globs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/timebomb-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/urls-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/validate_fields-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Hoe/with_config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/SshDirPublisher/cdesc-SshDirPublisher.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/Task/cdesc-Task.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/Task/comment-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/Task/plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/TaskManager/all_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/TaskManager/cdesc-TaskManager.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/all_tasks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/cdesc-Rake.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/clear_tasks-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/Rake/undo-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/String/rdoc_to_markdown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/page-History_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-3.13.1/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/History.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/Hoe.pdf
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/bin/sow
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/clean.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/compiler.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/debug.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/deps.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/flay.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/flog.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/gem_prelude_sucks.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/gemcutter.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/inline.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/newb.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/package.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/publish.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/racc.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/rake.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/rcov.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/rdoc.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/signing.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/lib/hoe/test.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/.autotest.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/History.txt.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/Manifest.txt.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/README.txt.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/Rakefile.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/bin/file_name.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/lib/file_name.rb.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/template/test/test_file_name.rb.erb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/test/test_hoe.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/test/test_hoe_debug.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/test/test_hoe_gemcutter.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/test/test_hoe_publish.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-3.13.1/test/test_hoe_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/hoe-3.13.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/sow
