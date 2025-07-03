# Health Analytics Dashboard

A comprehensive health analytics system with data input via command line and visualization via Streamlit.


### View Dashboard
Launch the Streamlit dashboard to visualize your data:
```bash
streamlit run streamlit_app.py
```

## 📊 Features

- **GitHub-style Heatmaps**: Visual representation of your sleep performance over 52 weeks
- **Performance Metrics**: Track sleep duration vs needs and sleep consistency
- **Dynamic Insights**: Automated performance analysis and recommendations
- **Rounded Visual Design**: Modern, clean heatmap visualization
- **Local Data Storage**: All data stored locally in CSV format

## 🗂️ File Structure

- \`main.py\`: Interactive data input script
- \`sleep.py\`: Data processing and grid creation logic
- \`streamlit_app.py\`: Web dashboard for visualization
- \`data.csv\`: Your health data storage (created automatically)

## 🎨 Visualization

The dashboard displays two main heatmaps:

### Sleep Hours vs Needed
Shows how well you're meeting your sleep duration requirements:
- **Dark Green**: Excellent (≥92.5%)
- **Medium Green**: Good (85-92.5%)
- **Light Green**: Adequate (77.5-85%)
- **Very Light Green**: Below optimal (70-77.5%)
- **Gray**: Insufficient (<70%)

### Sleep Consistency
Shows how consistent your sleep schedule is:
- **Dark Green**: Very consistent (≥90%)
- **Medium Green**: Good consistency (80-90%)
- **Light Green**: Moderate consistency (70-80%)
- **Very Light Green**: Poor consistency (60-70%)
- **Gray**: Very inconsistent (<60%)

## 📅 Heatmap Layout

- **Rows**: Monday (top) to Sunday (bottom)
- **Columns**: 52 weeks of data, with current week on the right
- **Colors**: Performance-based color coding with rounded corners

## 🔄 Workflow

1. **Daily Input**: Use \`python main.py\` to log your daily metrics
2. **Visualization**: Run \`streamlit run streamlit_app.py\` to view your progress
3. **Analysis**: Review insights and trends in the dashboard
4. **Repeat**: Continue logging data to build your health history

## 📋 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```