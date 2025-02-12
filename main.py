import json
file_name = "youtube.txt"

def open_files():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return[]

def write_files(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def display_videos(videos):
    enumerated_videos = enumerate(videos, start = 1)
    print("*"*50)
    print()
    for i, video in enumerated_videos:
        print(f"{i}. title: {video["name"]} duration: {video["time"]}")
    print()
    print("*"*50)

def insert_videos(videos):
    name = input("enter the video title: ")
    time = input("enter the video duration: ")
    videos.append({"name": name,"time": time})
    write_files(videos)
    print(f"\ninserted video with title {name} and time duration of {time}")

def update_old_videos(videos):
    display_videos(videos)
    index = int(input("enter the index of video to be updated: "))
    name = input("enter new title: ")
    time = input("enter new time duration: ")
    videos[index-1] = {"name": name,"time": time}
    write_files(videos)
    print(f"\nupdated video with title {name} and time duration of {time}")

def delete_video(videos):
    display_videos(videos)
    index = int(input("enter the index of video to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        write_files(videos)
    else:
        print("you entered invalid input")


def main():
    videos = open_files()
    while True:
        print()
        print("*** YOUTUBE WATCHLIST ***")
        print("1. Display youtube list")
        print("2. Insert New Video")
        print("3. update Old list")
        print("4. Delete a Youtube video")
        print("5. exit Youtube Watchlist")
        value = input("\nEnter a choice: ")

        match value:
            case "1":
                display_videos(videos)
            case "2":
                insert_videos(videos)   
            case "3":
                update_old_videos(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case default:
                print("invalid choice")


if __name__ == "__main__":
    main()