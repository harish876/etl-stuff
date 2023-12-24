from dags.kafka_stream import stream_data
def main():
    while True:
        stream_data()
    
if __name__ == '__main__':
    main()