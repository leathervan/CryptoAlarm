## Usage
Run the script with the following arguments:

```python script.py <crypto_pair> <operator> <price> <interval>```

### Arguments:
- `<crypto_pair>`: Trading pair (e.g., `BTC-USDT`).
- `<operator>`: Comparison operator, either `<` (alert if price drops) or `>` (alert if price rises).
- `<price>`: The threshold price to trigger the alert.
- `<interval>`: Request interval in seconds.

### Example:
Monitor ARB-USDT price and alert if it drops below 0.45 USDT, checking every 60 seconds:

```python alarm.py ARB-USDT "<" 0.45 60```

