multi_error_suppress:
	$(CXX) -w multi_error_suppress.cpp -o /dev/null
multi_error_suppress_cstyle:
	$(CXX) -w multi_error_suppress_cstyle.cpp -o /dev/null
multi_error_suppress_typo:
	$(CXX) -w multi_error_suppress_typo.cpp -o /dev/null
multi_error:
	$(CXX) -w multi_error.cpp -o /dev/null
nofail:
	$(CXX) -w nofail.cpp -o /dev/null
simple1:
	$(CXX) -w simple1.cpp -o /dev/null
simple2:
	$(CXX) -w simple2.cpp -o /dev/null
tidy_check:
	$(CXX) -w tidy_check.cpp -o /dev/null
saargs_forward:
	$(CXX) -w -std=c++11 saargs_forward.cpp -o /dev/null
source_code_comments:
	$(CXX) -w source_code_comments.cpp -Wno-unused-value -o /dev/null
deduplication:
	$(CXX) -w -DVAR=1 simple1.cpp -o /dev/null
	$(CXX) -w -DVAR=2 simple1.cpp -o /dev/null
compiler_warning_simple:
	$(CXX) -w compiler_warning.cpp -o /dev/null
compiler_warning_wno_simple:
	$(CXX) -w compiler_warning.cpp -Wno-unused-variable -o /dev/null
compiler_warning_wno_group:
	$(CXX) -w compiler_warning.cpp -Wno-unused -o /dev/null
compiler_warning_unused:
	$(CXX) -w compiler_warning.cpp -Wunused -o /dev/null
