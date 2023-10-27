c.ServerProxy.servers = {
   "test_panel": {
       "command": ["panel", "serve", "~/run.py", "--allow-websocket-origin=*", "--port", "{port}"]
   }
}
