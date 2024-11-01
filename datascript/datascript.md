path = avi.http.get_path()

if path == "/foo" then
  avi.vs.analytics.counter("foo", avi.vs.analytics.INCR)
  var = avi.vs.analytics.get_metric("foo", avi.vs.analytics.METRICTYPE_COUNTER)
  avi.vs.log("Foo = " .. var)
  avi.http.response(200, {content_type="text/html"}, "<html><body>Foo = " .. var .. "</body></html>")
end