# SentinelOne Removal Tool

This Python script provides a safe and efficient method for completely removing SentinelOne Agent from a Windows-based computer. It is especially useful in situations where the original SentinelOne management organization is no longer available, and official removal methods have failed.

---

## 🚨 Important Notice

- **Always create a system restore point and backup the registry before running this script.**
- **Run the script as Administrator to ensure successful execution.**
- **Restart the system immediately after script execution.**

---

## 🛠️ How to Use

### Step-by-Step Instructions:

1. **Download the script:**

```bash
git clone <repository-url>
```

2. **Navigate to the script location:**

```bash
cd SentinelOne-Removal-Tool
```

3. **Run the script (Administrator):**

```bash
python remove_sentinelone.py
```

4. **Restart your computer** to complete the removal process.

---

## ✅ Features

- Stops SentinelOne services safely.
- Kills all active SentinelOne processes.
- Removes SentinelOne files and drivers completely.
- Cleans SentinelOne-related registry keys.

---

## ⚠️ Disclaimer

Use this script at your own risk. While extensive precautions are implemented, the author is not responsible for any potential data loss or system instability. Ensure backups are performed before execution.

---

## 📌 Contributing

Contributions, suggestions, and issue reporting are welcome. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
