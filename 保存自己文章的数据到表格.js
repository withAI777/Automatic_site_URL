// ==UserScript==
// @name         保存自己文章的数据到表格
// @namespace    https://github.com/withAI777/en_state_demo_video
// @version      1.0
// @description  下载自己文章的url/Category/Date/Template/View Count到表格
// @author       Musk
// @match        https://www.**************.com/******/seo/articles?author=xxxx*
// @require      https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.17.4/xlsx.full.min.js
// @grant        none
// ==/UserScript==

/* global XLSX */

(function() {
    'use strict';

    // 函数：下载Excel文件
    function downloadExcel(data, filename) {
        // 将数据转换为工作表
        const ws = XLSX.utils.aoa_to_sheet(data);
        // 创建新的工作簿
        const wb = XLSX.utils.book_new();
        // 将工作表添加到工作簿中
        XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
        // 写入文件并下载
        XLSX.writeFile(wb, filename);
    }

    // 函数：获取下一页链接
    function getNextPageLink() {
        // 查找下一页链接元素
        const nextLink = document.querySelector('li.next > a');
        // 如果存在下一页链接，返回链接的href属性值，否则返回null
        return nextLink ? nextLink.href : null;
    }

    // 函数：提取数据并下载
    function extractDataAndDownload() {
        // 查找表格主体元素
        const tbody = document.querySelector('tbody');
        // 如果找不到表格主体元素，输出错误信息并返回
        if (!tbody) {
            console.error('Table body (tbody) not found');
            return;
        }

        // 获取所有行元素
        const rows = Array.from(tbody.querySelectorAll('tr'));
        // 创建一个数组，用于存储表格数据，包括标题行
        const data = [['url', 'category', 'Date', 'Template', 'View Count']];
        // 获取当前页面的基本URL
        const baseURL = window.location.origin;

        // 遍历每一行
        rows.forEach(row => {
            // 查找日期单元格、模板单元格和查看次数单元格
            const dateCell = row.querySelector('td:nth-child(4)');
            const templateCell = row.querySelector('td:nth-child(5)');
            const viewCountCell = row.querySelector('td:nth-child(7)');

            // 如果日期单元格、模板单元格和查看次数单元格都存在
            if (dateCell && templateCell && viewCountCell) {
                // 提取日期、模板和查看次数
                const date = dateCell.textContent.trim();
                const template = templateCell.textContent.trim();
                const viewCount = viewCountCell.textContent.trim();

                // 查找包含链接的元素
                const link = row.querySelector('.func_list a[href][target="_blank"]');
                // 如果链接存在
                if (link) {
                    // 获取链接的href属性值，并拼接为完整URL
                    const href = link.getAttribute('href');
                    const fullURL = baseURL + href;
                    // 提取分类信息
                    const category = row.querySelector('.category').textContent.trim();
                    // 将提取的数据添加到数组中
                    data.push([fullURL, category, date, template, viewCount]);
                }
            }
        });

        // 提取当前页码
        let currentPage = window.location.href.match(/page=(\d+)/);
        let pageNumber = currentPage ? currentPage[1] : 1;
        // 生成文件名
        let filename = pageNumber + '.xlsx';

        // 下载Excel文件
        downloadExcel(data, filename);

        // 获取下一页链接
        const nextPageLink = getNextPageLink();
        // 如果存在下一页链接，则跳转至下一页
        if (nextPageLink) {
            window.location.href = nextPageLink;
        }
    }

    // 调用函数提取数据并下载
    extractDataAndDownload();
})();
