# PySplit

PySplit is a Python library for communicating with Livesplit Server.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install livesplit-python
```

## Usage

### Example
```python
import livesplit
import time

# Create our livesplit object
# On connection, your timer won't be reset by default
# To read more, take a look at options later.

l = livesplit.Livesplit()

# Start our timer

l.startTimer()
l.startGameTimer()

# Wait one second
time.sleep(1)

# Stop the game timer 1 second in
l.stopGameTimer()

time.sleep(1)

# Stop the timer
l.pause()

# Wait one second again
time.sleep(1)

# Reset the timer

l.reset()
```

### Livesplit Parameters

| Parameter        | Type    | Description                                                          | Default          |
|------------------|---------|----------------------------------------------------------------------|------------------|
| `ip`             | String  | IP address / hostname the Livesplit Server can be located at.        | `"127.0.0.1"`    |
| `port`           | Integer | Port that the Livesplit Server is listening on.                      | `16834`          |
| `reset`          | Boolean | Whether to reset the timer when creating this object                 | `False`          |
| `setupGameTimer` | Boolean | Whether to setup and pause the game timer when creating this object. | Value of `reset` |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT license. To read more, open up the license file.