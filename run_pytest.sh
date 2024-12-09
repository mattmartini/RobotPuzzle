#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

source "$HOME/.bash/functions/utility_fns.sh"

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # yath stop
}

###   clear scrollback history
iterm_clear_buffer() {
  echo -e "\033]1337;ClearScrollback\x07"
}

usage() {
  cat <<EOHelp
  run_pytest <options>
    note: options need an argument
    --output   | -o  1   Show stdout and stderr of tests
    --verbose  | -v  1   Verbose output
    --cov      | -c  1   Produce a coverage report
    --html     | -h  1   Test output in html format
    --pretty   | -p  0   Turn off pretty reporting
    --random   | -r  0   Don't randomize order
    --fixtures | -f  1   Only show active fixures
    --setup    | -s  1   Only show pytest setup
    --help 1             This help message
EOHelp
exit 1
}

test_cmd=''

make_test_cmd() {
  local -A config
  config=(  [h]='html'     [html]=0 )
  config+=( [c]='cov'      [cov]=0 )
  config+=( [p]='pretty'   [pretty]=1 )
  config+=( [r]='random'   [random]=1 )
  config+=( [v]='verbose'  [verbose]=0 )
  config+=( [o]='output'   [output]=0 )
  config+=( [f]='fixtures' [fixtures]=0 )
  config+=( [s]='setup'    [setup]=0 )
  config+=(                [help]=0 )

  arg_parse "$@"

  local cmd='python -m pytest '
  local args=''

  if [[ ${config[help]} != 0 ]]; then
    usage
  fi

  if [[ ${config[cov]} != 0 ]]; then
    args+=' --cov=src --cov-branch --cov-report html'
  fi

  if [[ ${config[pretty]} != 1 ]]; then
    args+=' -p no:sugar '
  fi

  if [[ ${config[random]} != 0 ]]; then
    args+=' --random-order '
  fi

  if [[ ${config[verbose]} != 1 ]]; then
    args+=' --no-header '
  fi

  if [[ ${config[output]} != 0 ]]; then
    args+=' --capture=no '
  fi

  if [[ ${config[fixtures]} != 0 ]]; then
    args+=' --fixtures-per-test '
  fi

  if [[ ${config[setup]} != 0 ]]; then
    args+=' --setup-only '
  fi

  if [[ ${config[html]} != 0 ]]; then
    args+=' --html=tests/pytest_report.html ; open tests/pytest_report.html '
  fi

  test_cmd=$(printf "%s%s" "$cmd" "$args")
}

make_test_cmd "$@"
#echo "$test_cmd"


iterm_clear_buffer

eval " fd . 'src/' 'tests/'  -e py | entr $test_cmd"


