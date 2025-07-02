// Data - replace with your actual data
const hoursVsNeededGrid = [
    // First 48 weeks are empty (None values)
    ...Array(48).fill(null).map(() => Array(7).fill(null)),
    // Week 49: partial data
    [null, null, null, null, null, [0.18, 0.38, 0.188], [0.325, 0.635, 0.345]],
    // Week 50: full week
    [[0.729, 0.925, 0.749], [0.325, 0.635, 0.345], [0.427, 0.749, 0.455], [0.427, 0.749, 0.455], [0.325, 0.635, 0.345], [0.18, 0.38, 0.188], [0.941, 0.949, 0.961]],
    // Week 51: full week
    [[0.325, 0.635, 0.345], [0.18, 0.38, 0.188], [0.325, 0.635, 0.345], [0.729, 0.925, 0.749], [0.427, 0.749, 0.455], [0.325, 0.635, 0.345], [0.325, 0.635, 0.345]],
    // Week 52: partial data
    [[0.729, 0.925, 0.749], [0.729, 0.925, 0.749], null, null, null, null, null]
];

const sleepConsistencyGrid = [
    // First 48 weeks are empty (None values)
    ...Array(48).fill(null).map(() => Array(7).fill(null)),
    // Week 49: partial data
    [null, null, null, null, null, [0.941, 0.949, 0.961], [0.941, 0.949, 0.961]],
    // Week 50: full week
    [[0.427, 0.749, 0.455], [0.729, 0.925, 0.749], [0.325, 0.635, 0.345], [0.427, 0.749, 0.455], [0.325, 0.635, 0.345], [0.427, 0.749, 0.455], [0.941, 0.949, 0.961]],
    // Week 51: full week
    [[0.729, 0.925, 0.749], [0.427, 0.749, 0.455], [0.427, 0.749, 0.455], [0.325, 0.635, 0.345], [0.325, 0.635, 0.345], [0.427, 0.749, 0.455], [0.325, 0.635, 0.345]],
    // Week 52: partial data
    [[0.325, 0.635, 0.345], [0.427, 0.749, 0.455], null, null, null, null, null]
];

class HeatmapVisualizer {
    constructor() {
        this.tooltip = document.getElementById('tooltip');
        this.startDate = this.getStartDate();
        this.init();
    }

    getStartDate() {
        const today = new Date();
        const thisMonday = new Date(today);
        thisMonday.setDate(today.getDate() - today.getDay() + 1);
        const startDate = new Date(thisMonday);
        startDate.setDate(thisMonday.getDate() - 51 * 7);
        return startDate;
    }

    getDateForCell(week, day) {
        const date = new Date(this.startDate);
        date.setDate(this.startDate.getDate() + week * 7 + day);
        return date;
    }

    formatDate(date) {
        return date.toLocaleDateString('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
            year: 'numeric'
        });
    }

    getPerformanceLevel(rgb, metric) {
        if (!rgb) return { level: 'No data', range: '' };
        
        const [r, g, b] = rgb;
        
        if (metric === 'hours') {
            if (r < 0.2 && g < 0.4 && b < 0.2) return { level: 'Excellent', range: '(92.5%+)' };
            if (r < 0.35 && g < 0.65 && b < 0.35) return { level: 'Good', range: '(85-92.5%)' };
            if (r < 0.45 && g < 0.75 && b < 0.46) return { level: 'Fair', range: '(77.5-85%)' };
            if (r < 0.75 && g > 0.9 && b < 0.75) return { level: 'Poor', range: '(70-77.5%)' };
            return { level: 'Very Poor', range: '(<70%)' };
        } else {
            if (r < 0.2 && g < 0.4 && b < 0.2) return { level: 'Excellent', range: '(90%+)' };
            if (r < 0.35 && g < 0.65 && b < 0.35) return { level: 'Good', range: '(80-90%)' };
            if (r < 0.45 && g < 0.75 && b < 0.46) return { level: 'Fair', range: '(70-80%)' };
            if (r < 0.75 && g > 0.9 && b < 0.75) return { level: 'Poor', range: '(60-70%)' };
            return { level: 'Very Poor', range: '(<60%)' };
        }
    }

    getDataLevel(rgb) {
        if (!rgb) return 'none';
        
        const [r, g, b] = rgb;
        
        if (r < 0.2 && g < 0.4 && b < 0.2) return 'excellent';
        if (r < 0.35 && g < 0.65 && b < 0.35) return 'good';
        if (r < 0.45 && g < 0.75 && b < 0.46) return 'fair';
        if (r < 0.75 && g > 0.9 && b < 0.75) return 'poor';
        return 'very-poor';
    }

    rgbToString(rgb) {
        if (!rgb) return '#ebedf0';
        return `rgb(${Math.round(rgb[0] * 255)}, ${Math.round(rgb[1] * 255)}, ${Math.round(rgb[2] * 255)})`;
    }

    createMonthLabels(containerId) {
        const monthsContainer = document.getElementById(containerId);
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December'];
        const targetMonths = [0, 3, 6, 9]; // Jan, Apr, Jul, Oct (0-indexed)
        
        monthsContainer.innerHTML = '';
        
        let currentMonth = this.startDate.getMonth();
        
        for (let week = 0; week < 52; week++) {
            const weekDate = new Date(this.startDate);
            weekDate.setDate(this.startDate.getDate() + week * 7);
            const weekMonth = weekDate.getMonth();
            
            if ((weekMonth !== currentMonth || week === 0) && targetMonths.includes(weekMonth)) {
                const monthLabel = document.createElement('div');
                monthLabel.className = 'month-label';
                monthLabel.textContent = months[weekMonth];
                
                // Calculate position as percentage of total width
                const position = (week / 52) * 100;
                monthLabel.style.left = `${position}%`;
                
                monthsContainer.appendChild(monthLabel);
            }
            currentMonth = weekMonth;
        }
    }

    createGrid(gridId, data, metric) {
        const grid = document.getElementById(gridId);
        grid.innerHTML = '';
        
        const today = new Date().toDateString();
        
        // Create cells in column-major order (weeks as columns)
        for (let week = 0; week < 52; week++) {
            for (let day = 0; day < 7; day++) {
                const cell = document.createElement('div');
                cell.className = 'cell';
                
                const cellData = data[week] ? data[week][day] : null;
                const cellDate = this.getDateForCell(week, day);
                const dataLevel = this.getDataLevel(cellData);
                
                cell.setAttribute('data-level', dataLevel);
                cell.style.gridColumn = week + 1;
                cell.style.gridRow = day + 1;
                
                // Mark today's cell
                if (cellDate.toDateString() === today) {
                    cell.classList.add('today');
                }
                
                // Add hover events
                cell.addEventListener('mouseenter', (e) => this.showTooltip(e, cellDate, cellData, metric));
                cell.addEventListener('mouseleave', () => this.hideTooltip());
                
                grid.appendChild(cell);
            }
        }
    }

    showTooltip(event, date, data, metric) {
        const performance = this.getPerformanceLevel(data, metric);
        
        this.tooltip.innerHTML = `
            <div class="tooltip-date">${this.formatDate(date)}</div>
            <div class="tooltip-performance">${performance.level} ${performance.range}</div>
        `;
        
        const rect = event.target.getBoundingClientRect();
        const tooltipRect = this.tooltip.getBoundingClientRect();
        
        let left = rect.left + rect.width / 2;
        let top = rect.top - 10;
        
        // Adjust if tooltip would go off screen
        if (left + tooltipRect.width / 2 > window.innerWidth) {
            left = window.innerWidth - tooltipRect.width / 2 - 10;
        }
        if (left - tooltipRect.width / 2 < 0) {
            left = tooltipRect.width / 2 + 10;
        }
        
        this.tooltip.style.left = `${left}px`;
        this.tooltip.style.top = `${top}px`;
        this.tooltip.classList.add('visible');
    }

    hideTooltip() {
        this.tooltip.classList.remove('visible');
    }

    init() {
        // Create month labels for both heatmaps
        this.createMonthLabels('months-hours');
        this.createMonthLabels('months-sleep');
        
        // Create both grids
        this.createGrid('grid-hours', hoursVsNeededGrid, 'hours');
        this.createGrid('grid-sleep', sleepConsistencyGrid, 'sleep');
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new HeatmapVisualizer();
});