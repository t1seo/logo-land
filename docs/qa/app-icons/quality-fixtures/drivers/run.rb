require 'timeout'
require 'json'
name, limit, *cmd = ARGV
root = '/tmp/ll-icon-quality-core'
log = "docs/qa/app-icons/quality-fixtures/#{name}.log"
File.open("#{root}/processes.jsonl", 'a') { |f| f.puts JSON.generate({name: name, command: cmd, timeout: limit.to_i, state: 'registered'}) }
File.open(log, 'w') do |file|
  pid = Process.spawn({'PYTHONDONTWRITEBYTECODE'=>'1', 'RUFF_CACHE_DIR'=>"#{root}/ruff-cache"}, *cmd, out: file, err: file, pgroup: true)
  File.open("#{root}/processes.jsonl", 'a') { |f| f.puts JSON.generate({name: name, pid: pid, state: 'started'}) }
  begin
    _, status = Timeout.timeout(limit.to_i) { Process.wait2(pid) }
    File.open("#{root}/processes.jsonl", 'a') { |f| f.puts JSON.generate({name: name, pid: pid, exit: status.exitstatus, state: 'finished'}) }
    puts "#{name}: exit #{status.exitstatus}; #{log}"
    puts File.read(log).lines.last(12)
    exit status.exitstatus
  rescue Timeout::Error
    Process.kill('TERM', -pid)
    Process.wait(pid)
    abort "#{name}: timeout after #{limit}s"
  end
end
