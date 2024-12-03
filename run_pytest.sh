#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

source "$HOME/.bash/functions/utility_fns.sh"

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # yath stop
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

  arg_parse "$@"

  local cmd='python -m pytest '
  local args=''

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


eval " fd . 'src/' 'tests/'  -e py | entr $test_cmd"


