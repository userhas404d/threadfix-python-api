import threadfixpro

api = threadfixpro.ThreadFixProAPI('http://localhost:8081/threadfix/', '5bi08XUPA9wdTEnS0wnNx8SaD8llyfwCg8O2SBetGyF4', verify_ssl=False, debug=True)#make api handler note url must end in a slash

print(api.create_application_version('test89', '2019-06-20', 1))
