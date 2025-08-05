local xff_header = avi.http.get_header('x-forwarded-for')
local tcip_header = avi.http.get_header('true-client-ip')

if xff_header == nil and tcip_header == nil then
  local client_ip = avi.vs.client_ip()
  avi.http.add_header('x-forwarded-for', client_ip)
end
