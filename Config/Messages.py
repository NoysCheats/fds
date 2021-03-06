from Config.Singleton import Singleton
from Config.Configs import Configs


class Messages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            configs = Configs()
            self.STARTUP_MESSAGE = 'Starting Vulkan...'
            self.STARTUP_COMPLETE_MESSAGE = 'Vulkan is now operating.'

            self.SONGINFO_UPLOADER = "Uploader: "
            self.SONGINFO_DURATION = "Duration: "
            self.SONGINFO_REQUESTER = 'Requester: '
            self.SONGINFO_POSITION = 'Position: '

            self.SONGS_ADDED = 'You added {} songs to the queue'
            self.SONG_ADDED = 'You added the song `{}` to the queue'
            self.SONG_ADDED_TWO = 'π§ Song added to the queue'
            self.SONG_PLAYING = 'π§ Song playing now'
            self.SONG_PLAYER = 'π§ Song Player'
            self.QUEUE_TITLE = 'π§ Songs in Queue'
            self.ONE_SONG_LOOPING = 'π§ Looping One Song'
            self.ALL_SONGS_LOOPING = 'π§ Looping All Songs'
            self.SONG_PAUSED = 'βΈοΈ Song paused'
            self.SONG_RESUMED = 'βΆοΈ Song playing'
            self.EMPTY_QUEUE = f'π Song queue is empty, use {configs.BOT_PREFIX}play to add new songs'
            self.SONG_DOWNLOADING = 'π₯ Downloading...'

            self.HISTORY_TITLE = 'π§ Played Songs'
            self.HISTORY_EMPTY = 'π There is no musics in history'

            self.SONG_MOVED_SUCCESSFULLY = 'Song `{}` in position `{}` moved to the position `{}` successfully'
            self.SONG_REMOVED_SUCCESSFULLY = 'Song `{}` removed successfully'

            self.LOOP_ALL_ON = f'β Vulkan is looping all songs, use {configs.BOT_PREFIX}loop off to disable this loop first'
            self.LOOP_ONE_ON = f'β Vulkan is looping one song, use {configs.BOT_PREFIX}loop off to disable this loop first'
            self.LOOP_ALL_ALREADY_ON = 'π Vulkan is already looping all songs'
            self.LOOP_ONE_ALREADY_ON = 'π Vulkan is already looping the current song'
            self.LOOP_ALL_ACTIVATE = 'π Looping all songs'
            self.LOOP_ONE_ACTIVATE = 'π Looping the current song'
            self.LOOP_DISABLE = 'β‘οΈ Loop disabled'
            self.LOOP_ALREADY_DISABLE = 'β Loop is already disabled'
            self.LOOP_ON = f'β This command cannot be invoked with any loop activated. Use {configs.BOT_PREFIX}loop off to disable loop'

            self.SONGS_SHUFFLED = 'π Songs shuffled successfully'
            self.ERROR_SHUFFLING = 'β Error while shuffling the songs'
            self.ERROR_MOVING = 'β Error while moving the songs'
            self.LENGTH_ERROR = 'β Numbers must be between 1 and queue length, use -1 for the last song'
            self.ERROR_NUMBER = 'β This command require a number'
            self.ERROR_PLAYING = 'β Error while playing songs'
            self.COMMAND_NOT_FOUND = f'β Command not found, type {configs.BOT_PREFIX}help to see all commands'
            self.UNKNOWN_ERROR = f'β Unknown Error, if needed, use {configs.BOT_PREFIX}reset to reset the player of your server'
            self.ERROR_MISSING_ARGUMENTS = f'β Missing arguments in this command. Type {configs.BOT_PREFIX}help "command" to see more info about this command'
            self.NOT_PREVIOUS = 'β There is none previous song to play'
            self.PLAYER_NOT_PLAYING = f'β No song playing. Use {configs.BOT_PREFIX}play to start the player'
            self.IMPOSSIBLE_MOVE = 'That is impossible :('
            self.ERROR_TITLE = 'Error :-('
            self.NO_CHANNEL = 'To play some music, connect to any voice channel first.'
            self.NO_GUILD = f'This server does not has a Player, try {configs.BOT_PREFIX}reset'
            self.INVALID_INPUT = f'This type of input was too strange, try something better or type {configs.BOT_PREFIX}help play'
            self.DOWNLOADING_ERROR = 'β An error occurred while downloading'
            self.EXTRACTING_ERROR = 'β An error ocurred while searching for the songs'

            self.MY_ERROR_BAD_COMMAND = 'This string serves to verify if some error was raised by myself on purpose'
            self.BAD_COMMAND_TITLE = 'Misuse of command'
            self.BAD_COMMAND = f'β Bad usage of this command, type {configs.BOT_PREFIX}help "command" to understand the command better'
            self.VIDEO_UNAVAILABLE = 'β Sorry. This video is unavailable for download.'
            self.ERROR_DUE_LOOP_ONE_ON = f'β This command cannot be executed with loop one activated. Use {configs.BOT_PREFIX}loop off to disable loop.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = Configs()
            self.UNKNOWN_INPUT = f'This type of input was too strange, try something else or type {config.BOT_PREFIX}help play'
            self.UNKNOWN_INPUT_TITLE = 'Nothing Found'
            self.SPOTIFY_ERROR = 'Spotify could not process any songs with this input, verify your link or try again later.'
            self.GENERIC_TITLE = 'Input could not be processed'
            self.YOUTUBE_ERROR = 'Youtube could not process any songs with this input, verify your link or try again later.'
