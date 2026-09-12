require 'json'
require 'digest'
require 'fileutils'
require 'timeout'
manual = File.read('/tmp/ll-icon-quality-core/manual.rb').split('plan = JSON.parse',2).first
manual = manual.sub('TRANSCRIPT = []','TRANSCRIPT = JSON.parse(File.read("#{EVIDENCE}/cli-transcript.json"), symbolize_names: true)')
eval(manual,TOPLEVEL_BINDING,'registered manual CLI helper')
workspace = '/tmp/ll-icon-quality-core/workspaces/strict-soft'
protected = Dir.glob("#{workspace}/**/*",File::FNM_DOTMATCH).select { |p| File.file?(p) }.sort.to_h { |p| [p,Digest::SHA256.file(p).hexdigest] }
malformed = save('truncated-icon',nil)
File.write(malformed,'{"preset":')
result = cli('truncated-json-no-tree-writes',workspace,'prompt','--session','strict-soft','--app-icon-file',malformed,expected:1)
check(result.include?('json_invalid'),'truncated JSON rejected')
after = Dir.glob("#{workspace}/**/*",File::FNM_DOTMATCH).select { |p| File.file?(p) }.sort.to_h { |p| [p,Digest::SHA256.file(p).hexdigest] }
check(after == protected,'malformed input preserves complete workspace tree')
workspace = '/tmp/ll-icon-quality-core/workspaces/parent-null'
folder = "#{workspace}/.logo-generator/sessions/demo"
FileUtils.mkdir_p("#{folder}/artifacts")
FileUtils.cp('docs/qa/app-icons/core-fixtures/synthetic-baseline.png',"#{folder}/artifacts/v1.png")
state = JSON.parse(File.read('docs/qa/app-icons/core-fixtures/session-v2.json'))
state['brief'] = JSON.parse(File.read('/tmp/ll-icon-quality-core/strict-soft-brief.json'))
state_path = "#{folder}/session.json"
File.write(state_path,JSON.pretty_generate(state)+"\n")
before = File.binread(state_path)
result = cli('legacy-parent-null',workspace,'prompt','--session','demo','--parent','v1','--changes','Preserve the original')
check(result['app_icon'].nil? && result['requested_background'].nil?,'legacy parent-null wins over icon brief')
check(result.fetch('mode') == 'edit' && result.fetch('parent_id') == 'v1','legacy edit binding')
check(File.binread(state_path) == before,'parent-null read preserves exact state')
expected = result
3.times do |i|
  result = cli("parent-null-resume-#{i}",workspace,'prompt','--session','demo','--parent','v1','--changes','Preserve the original')
  check(result == expected && File.binread(state_path) == before,'repeat parent-null prompt unchanged')
end
puts 'PASS: complete-tree no-write rejection, legacy parent-null, and three exact fresh-process legacy read repetitions.'
