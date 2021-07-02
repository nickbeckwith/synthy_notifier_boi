import synth_notify.synth_notify as sn
import argparse

def main():
    # parse arguments
    parser = argparse.ArgumentParser(
                        description='Notify discord webhook with a '
                                    'meme from r/fpga')
    parser.add_argument('status', type=int, metavar='$?',
                        help='Well behaved status code ($?)')
    parser.add_argument('-u', '--url', type=str, required=True,
                        help='Discord webhook URL')
    parser.add_argument('-m', '--message', type=str, required=True,
                        help='Message to send to webhook')
    parser.add_argument('-f', '--failure', type=str,
                        help='Message to send to webhook instead of '
                             '--message if status code shows failure')
    args = parser.parse_args()

    # prep and call
    success = args.status == 0
    status = sn.notify(success, args.url, args.message, args.failure)
    return status
