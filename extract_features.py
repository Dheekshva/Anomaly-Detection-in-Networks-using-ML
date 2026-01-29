import pyshark
import csv

def extract_features(pcap_file, output_csv):
    cap = pyshark.FileCapture(pcap_file)
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['source', 'destination', 'protocol', 'length', 'info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for pkt in cap:
            try:
                writer.writerow({
                    'source': pkt.ip.src,
                    'destination': pkt.ip.dst,
                    'protocol': pkt.transport_layer,
                    'length': pkt.length,
                    'info': pkt.highest_layer
                })
            except AttributeError:
                continue
