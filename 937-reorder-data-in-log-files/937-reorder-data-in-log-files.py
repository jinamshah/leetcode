import re
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, log_data = log.split(" ",1)
            if re.match(r'\d+', log_data):
                digit_logs.append(log)
            else:
                letter_logs.append([identifier,log_data])
        print(letter_logs)
        # letter_logs = dict(sorted(letter_logs.items(), key = lambda kv:kv[1], kv[0]))
        letter_logs = sorted(letter_logs, key = lambda x: (x[1],x[0]))
        letter_logs = [k+" "+v for k,v in letter_logs]
        return letter_logs + digit_logs