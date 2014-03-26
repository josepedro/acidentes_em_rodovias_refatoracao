/*
 * Universidade de Brasilia - FGA
 * Técnicas de Programação, 1/2014
 * Acidentes em Rodovias, 2013-2014
 * GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
 */
/*
 Map plugin v0.1 for Highcharts

 (c) 2011-2013 Torstein Hønsi

 License: www.highcharts.com/license
*/
(function (j) {
    function D(a, b, c) {
        for (var d = 4, e, f = []; d--;) e = b.rgba[d] + (a.rgba[d] - b.rgba[d]) * (1 - c), f[d] = d === 3 ? e : Math.round(e);
        return "rgba(" + f.join(",") + ")"
    }

    function E(a, b, c, d, e, f, k, g, h) {
        a = a["stroke-width"] % 2 / 2;
        b -= a;
        c -= a;
        return ["M", b + f, c, "L", b + d - k, c, "C", b + d - k / 2, c, b + d, c + k / 2, b + d, c + k, "L", b + d, c + e - g, "C", b + d, c + e - g / 2, b + d - g / 2, c + e, b + d - g, c + e, "L", b + h, c + e, "C", b + h / 2, c + e, b, c + e - h / 2, b, c + e - h, "L", b, c + f, "C", b, c + f / 2, b + f / 2, c, b + f, c, "Z"]
    }
    var t = j.Axis,
        z = j.Chart,
        u = j.Point,
        A = j.Pointer,
        F = j.VMLRenderer,
        B = j.SVGRenderer.prototype.symbols,
        m = j.each,
        v = j.extend,
        r = j.extendClass,
        p = j.merge,
        i = j.pick,
        G = j.numberFormat,
        C = j.getOptions(),
        l = j.seriesTypes,
        H = HighchartsAdapter.inArray,
        q = C.plotOptions,
        w = j.wrap,
        y = j.Color,
        s = function () {};
    v(C.lang, {
        zoomIn: "Zoom in",
        zoomOut: "Zoom out"
    });
    C.mapNavigation = {
        buttonOptions: {
            alignTo: "plotBox",
            align: "left",
            verticalAlign: "top",
            x: 0,
            width: 18,
            height: 18,
            style: {
                fontSize: "15px",
                fontWeight: "bold",
                textAlign: "center"
            },
            theme: {
                "stroke-width": 1
            }
        },
        buttons: {
            zoomIn: {
                onclick: function () {
                    this.mapZoom(0.5)
                },
                text: "+",
                y: 0
            },
            zoomOut: {
                onclick: function () {
                    this.mapZoom(2)
                },
                text: "-",
                y: 28
            }
        }
    };
    j.splitPath = function (a) {
        var b, a = a.replace(/([A-Za-z])/g, " $1 "),
            a = a.replace(/^\s*/, "").replace(/\s*$/, ""),
            a = a.split(/[ ,]+/);
        for (b = 0; b < a.length; b++) /[a-zA-Z]/.test(a[b]) || (a[b] = parseFloat(a[b]));
        return a
    };
    j.maps = {};
    w(t.prototype, "getSeriesExtremes", function (a) {
        var b = this.isXAxis,
            c, d, e = [];
        b && m(this.series, function (a, b) {
            if (a.useMapGeometry) e[b] = a.xData, a.xData = []
        });
        a.call(this);
        if (b) c = i(this.dataMin, Number.MAX_VALUE), d = i(this.dataMax, Number.MIN_VALUE), m(this.series, function (a, b) {
            if (a.useMapGeometry) c =
                Math.min(c, i(a.minX, c)), d = Math.max(d, i(a.maxX, c)), a.xData = e[b]
        }), this.dataMin = c, this.dataMax = d
    });
    w(t.prototype, "setAxisTranslation", function (a) {
        var b = this.chart,
            c = b.plotWidth / b.plotHeight,
            d = this.isXAxis,
            e = b.xAxis[0];
        a.call(this);
        if (b.options.chart.type === "map" && !d && e.transA !== void 0) this.transA = e.transA = Math.min(this.transA, e.transA), a = (e.max - e.min) / (this.max - this.min), e = a > c ? this : e, c = (e.max - e.min) * e.transA, e.minPixelPadding = (e.len - c) / 2
    });
    w(z.prototype, "render", function (a) {
        var b = this,
            c = b.options.mapNavigation;
        a.call(b);
        b.renderMapNavigation();
        (i(c.enableDoubleClickZoom, c.enabled) || c.enableDoubleClickZoomTo) && j.addEvent(b.container, "dblclick", function (a) {
            b.pointer.onContainerDblClick(a)
        });
        i(c.enableMouseWheelZoom, c.enabled) && j.addEvent(b.container, document.onmousewheel === void 0 ? "DOMMouseScroll" : "mousewheel", function (a) {
            b.pointer.onContainerMouseWheel(a)
        })
    });
    v(A.prototype, {
        onContainerDblClick: function (a) {
            var b = this.chart,
                a = this.normalize(a);
            b.options.mapNavigation.enableDoubleClickZoomTo ? b.pointer.inClass(a.target,
                "highcharts-tracker") && b.zoomToShape(b.hoverPoint) : b.isInsidePlot(a.chartX - b.plotLeft, a.chartY - b.plotTop) && b.mapZoom(0.5, b.xAxis[0].toValue(a.chartX), b.yAxis[0].toValue(a.chartY))
        },
        onContainerMouseWheel: function (a) {
            var b = this.chart,
                c, a = this.normalize(a);
            c = a.detail || -(a.wheelDelta / 120);
            b.isInsidePlot(a.chartX - b.plotLeft, a.chartY - b.plotTop) && b.mapZoom(c > 0 ? 2 : 0.5, b.xAxis[0].toValue(a.chartX), b.yAxis[0].toValue(a.chartY))
        }
    });
    w(A.prototype, "init", function (a, b, c) {
        a.call(this, b, c);
        if (i(c.mapNavigation.enableTouchZoom,
            c.mapNavigation.enabled)) this.pinchX = this.pinchHor = this.pinchY = this.pinchVert = !0
    });
    w(A.prototype, "pinchTranslate", function (a, b, c, d, e, f, k, g, h) {
        a.call(this, b, c, d, e, f, k, g, h);
        this.chart.options.chart.type === "map" && (a = f.scaleX > f.scaleY, this.pinchTranslateDirection(!a, d, e, f, k, g, h, a ? f.scaleX : f.scaleY))
    });
    v(z.prototype, {
        renderMapNavigation: function () {
            var a = this,
                b = this.options.mapNavigation,
                c = b.buttons,
                d, e, f, k, g = function () {
                    this.handler.call(a)
                };
            if (i(b.enableButtons, b.enabled))
                for (d in c)
                    if (c.hasOwnProperty(d)) f =
                        p(b.buttonOptions, c[d]), e = f.theme, k = e.states, e = a.renderer.button(f.text, 0, 0, g, e, k && k.hover, k && k.select, 0, d === "zoomIn" ? "topbutton" : "bottombutton").attr({
                            width: f.width,
                            height: f.height,
                            title: a.options.lang[d],
                            zIndex: 5
                        }).css(f.style).add(), e.handler = f.onclick, e.align(v(f, {
                            width: e.width,
                            height: 2 * e.height
                        }), null, f.alignTo)
        },
        fitToBox: function (a, b) {
            m([
                ["x", "width"],
                ["y", "height"]
            ], function (c) {
                var d = c[0],
                    c = c[1];
                a[d] + a[c] > b[d] + b[c] && (a[c] > b[c] ? (a[c] = b[c], a[d] = b[d]) : a[d] = b[d] + b[c] - a[c]);
                a[c] > b[c] && (a[c] = b[c]);
                a[d] < b[d] && (a[d] = b[d])
            });
            return a
        },
        mapZoom: function (a, b, c) {
            if (!this.isMapZooming) {
                var d = this,
                    e = d.xAxis[0],
                    f = e.max - e.min,
                    k = i(b, e.min + f / 2),
                    b = f * a,
                    f = d.yAxis[0],
                    g = f.max - f.min,
                    c = i(c, f.min + g / 2);
                a *= g;
                k -= b / 2;
                g = c - a / 2;
                c = i(d.options.chart.animation, !0);
                b = d.fitToBox({
                    x: k,
                    y: g,
                    width: b,
                    height: a
                }, {
                    x: e.dataMin,
                    y: f.dataMin,
                    width: e.dataMax - e.dataMin,
                    height: f.dataMax - f.dataMin
                });
                e.setExtremes(b.x, b.x + b.width, !1);
                f.setExtremes(b.y, b.y + b.height, !1);
                if (e = c ? c.duration || 500 : 0) d.isMapZooming = !0, setTimeout(function () {
                    d.isMapZooming = !1
                }, e);
                d.redraw()
            }
        },
        zoomToShape: function (a) {
            var b = a.series,
                c = b.chart;
            b.xAxis.setExtremes(a._minX, a._maxX, !1);
            b.yAxis.setExtremes(a._minY, a._maxY, !1);
            c.redraw()
        }
    });
    q.map = p(q.scatter, {
        animation: !1,
        nullColor: "#F8F8F8",
        borderColor: "silver",
        borderWidth: 1,
        marker: null,
        stickyTracking: !1,
        dataLabels: {
            verticalAlign: "middle"
        },
        turboThreshold: 0,
        tooltip: {
            followPointer: !0,
            pointFormat: "{point.name}: {point.y}<br/>"
        },
        states: {
            normal: {
                animation: !0
            }
        }
    });
    t = r(u, {
        applyOptions: function (a, b) {
            var c = u.prototype.applyOptions.call(this,
                a, b),
                d = this.series,
                e = d.options,
                f = e.dataJoinBy;
            if (f && e.mapData)
                if (e = d.getMapData(f, c[f])) {
                    if (d.xyFromShape) c.x = e._midX, c.y = e._midY;
                    v(c, e)
                } else c.y = c.y || null;
            return c
        },
        setVisible: function (a) {
            var b = this,
                c = a ? "show" : "hide";
            m(["graphic", "dataLabel"], function (a) {
                if (b[a]) b[a][c]()
            })
        },
        onMouseOver: function (a) {
            clearTimeout(this.colorInterval);
            u.prototype.onMouseOver.call(this, a)
        },
        onMouseOut: function () {
            var a = this,
                b = +new Date,
                c = y(a.options.color),
                d = y(a.pointAttr.hover.fill),
                e = a.series.options.states.normal.animation,
                f = e && (e.duration || 500);
            if (f && c.rgba.length === 4 && d.rgba.length === 4) delete a.pointAttr[""].fill, clearTimeout(a.colorInterval), a.colorInterval = setInterval(function () {
                var e = (new Date - b) / f,
                    g = a.graphic;
                e > 1 && (e = 1);
                g && g.attr("fill", D(d, c, e));
                e >= 1 && clearTimeout(a.colorInterval)
            }, 13);
            u.prototype.onMouseOut.call(a)
        }
    });
    l.map = r(l.scatter, {
        type: "map",
        pointAttrToOptions: {
            stroke: "borderColor",
            "stroke-width": "borderWidth",
            fill: "color"
        },
        colorKey: "y",
        pointClass: t,
        trackerGroups: ["group", "markerGroup", "dataLabelsGroup"],
        getSymbol: s,
        supportsDrilldown: !0,
        getExtremesFromAll: !0,
        useMapGeometry: !0,
        init: function (a) {
            var b = this,
                c = a.options.legend,
                d = c.valueDecimals,
                e = c.valueSuffix || "",
                f = [],
                k, g, h, i, n, o;
            n = a.options.legend.layout === "horizontal";
            j.Series.prototype.init.apply(this, arguments);
            i = b.options.colorRange;
            if (c = b.options.valueRanges) m(c, function (c, i) {
                var n = !0;
                g = c.from;
                h = c.to;
                k = "";
                g === void 0 ? k = "< " : h === void 0 && (k = "> ");
                g !== void 0 && (k += G(g, d) + e);
                g !== void 0 && h !== void 0 && (k += " - ");
                h !== void 0 && (k += G(h, d) + e);
                f.push(j.extend({
                    chart: b.chart,
                    name: k,
                    options: {},
                    drawLegendSymbol: l.area.prototype.drawLegendSymbol,
                    visible: !0,
                    setState: s,
                    setVisible: function () {
                        n = this.visible = !n;
                        m(b.points, function (a) {
                            a.valueRange === i && a.setVisible(n)
                        });
                        a.legend.colorizeItem(this, n)
                    }
                }, c))
            }), b.legendItems = f;
            else if (i) g = i.from, h = i.to, c = i.fromLabel, i = i.toLabel, o = n ? [0, 0, 1, 0] : [0, 1, 0, 0], n || (n = c, c = i, i = n), n = {
                linearGradient: {
                    x1: o[0],
                    y1: o[1],
                    x2: o[2],
                    y2: o[3]
                },
                stops: [
                    [0, g],
                    [1, h]
                ]
            }, f = [{
                chart: b.chart,
                options: {},
                fromLabel: c,
                toLabel: i,
                color: n,
                drawLegendSymbol: this.drawLegendSymbolGradient,
                visible: !0,
                setState: s,
                setVisible: s
            }], b.legendItems = f
        },
        drawLegendSymbol: l.area.prototype.drawLegendSymbol,
        drawLegendSymbolGradient: function (a, b) {
            var c = a.options.symbolPadding,
                d = i(a.options.padding, 8),
                e, f, k = this.chart.renderer.fontMetrics(a.options.itemStyle.fontSize).h,
                g = a.options.layout === "horizontal",
                h;
            h = i(a.options.rectangleLength, 200);
            g ? (e = -(c / 2), f = 0) : (e = -h + a.baseline - c / 2, f = d + k);
            b.fromText = this.chart.renderer.text(b.fromLabel, f, e).attr({
                zIndex: 2
            }).add(b.legendGroup);
            f = b.fromText.getBBox();
            b.legendSymbol =
                this.chart.renderer.rect(g ? f.x + f.width + c : f.x - k - c, f.y, g ? h : k, g ? k : h, 2).attr({
                    zIndex: 1
                }).add(b.legendGroup);
            h = b.legendSymbol.getBBox();
            b.toText = this.chart.renderer.text(b.toLabel, h.x + h.width + c, g ? e : h.y + h.height - c).attr({
                zIndex: 2
            }).add(b.legendGroup);
            e = b.toText.getBBox();
            g ? (a.offsetWidth = f.width + h.width + e.width + c * 2 + d, a.itemY = k + d) : (a.offsetWidth = Math.max(f.width, e.width) + c + h.width + d, a.itemY = h.height + d, a.itemX = c)
        },
        getBox: function (a) {
            var b = Number.MIN_VALUE,
                c = Number.MAX_VALUE,
                d = Number.MIN_VALUE,
                e = Number.MAX_VALUE,
                f;
            m(a || [], function (a) {
                if (a.path) {
                    if (typeof a.path === "string") a.path = j.splitPath(a.path);
                    var g = a.path || [],
                        h = g.length,
                        l = !1,
                        n = Number.MIN_VALUE,
                        o = Number.MAX_VALUE,
                        m = Number.MIN_VALUE,
                        x = Number.MAX_VALUE;
                    if (!a._foundBox) {
                        for (; h--;) typeof g[h] === "number" && !isNaN(g[h]) && (l ? (n = Math.max(n, g[h]), o = Math.min(o, g[h])) : (m = Math.max(m, g[h]), x = Math.min(x, g[h])), l = !l);
                        a._midX = o + (n - o) * i(a.middleX, 0.5);
                        a._midY = x + (m - x) * i(a.middleY, 0.5);
                        a._maxX = n;
                        a._minX = o;
                        a._maxY = m;
                        a._minY = x;
                        a._foundBox = !0
                    }
                    b = Math.max(b, a._maxX);
                    c = Math.min(c,
                        a._minX);
                    d = Math.max(d, a._maxY);
                    e = Math.min(e, a._minY);
                    f = !0
                }
            });
            if (f) this.minY = Math.min(e, i(this.minY, Number.MAX_VALUE)), this.maxY = Math.max(d, i(this.maxY, Number.MIN_VALUE)), this.minX = Math.min(c, i(this.minX, Number.MAX_VALUE)), this.maxX = Math.max(b, i(this.maxX, Number.MIN_VALUE))
        },
        getExtremes: function () {
            this.dataMin = this.minY;
            this.dataMax = this.maxY
        },
        translatePath: function (a) {
            var b = !1,
                c = this.xAxis,
                d = this.yAxis,
                e, a = [].concat(a);
            for (e = a.length; e--;) typeof a[e] === "number" && (a[e] = b ? c.translate(a[e]) : d.len - d.translate(a[e]),
                b = !b);
            return a
        },
        setData: function (a, b) {
            var c = this.options,
                d = c.mapData,
                e = c.dataJoinBy,
                f = [];
            this.getBox(a);
            this.getBox(d);
            c.allAreas && d && (a = a || [], e && m(a, function (a) {
                f.push(a[e])
            }), m(d, function (b) {
                (!e || H(b[e], f) === -1) && a.push(p(b, {
                    y: null
                }))
            }));
            j.Series.prototype.setData.call(this, a, b)
        },
        getMapData: function (a, b) {
            var c = this.options.mapData,
                d = this.mapMap,
                e = c.length;
            if (!d) d = this.mapMap = [];
            if (d[b] !== void 0) return c[d[b]];
            else if (b !== void 0)
                for (; e--;)
                    if (c[e][a] === b) return d[b] = e, c[e]
        },
        translate: function () {
            var a =
                this,
                b = Number.MAX_VALUE,
                c = Number.MIN_VALUE;
            a.generatePoints();
            m(a.data, function (d) {
                d.shapeType = "path";
                d.shapeArgs = {
                    d: a.translatePath(d.path)
                };
                if (typeof d.y === "number")
                    if (d.y > c) c = d.y;
                    else if (d.y < b) b = d.y
            });
            a.translateColors(b, c)
        },
        translateColors: function (a, b) {
            var c = this.options,
                d = c.valueRanges,
                e = c.colorRange,
                f = this.colorKey,
                k = c.nullColor,
                g, h;
            e && (g = y(e.from), h = y(e.to));
            m(this.data, function (c) {
                var i = c[f],
                    j = i === null,
                    l, m;
                if (d)
                    if (m = d.length, j) l = k;
                    else {
                        for (; m--;)
                            if (j = d[m], g = j.from, h = j.to, (g === void 0 || i >=
                                g) && (h === void 0 || i <= h)) {
                                l = j.color;
                                break
                            }
                        c.valueRange = m
                    } else e && !j ? (i = 1 - (b - i) / (b - a), l = D(g, h, i)) : j && (l = k);
                if (l) c.color = null, c.options.color = l
            })
        },
        drawGraph: s,
        drawDataLabels: s,
        drawPoints: function () {
            var a = this.xAxis,
                b = this.yAxis,
                c = this.colorKey;
            m(this.data, function (a) {
                a.plotY = 1;
                if (a[c] === null) a[c] = 0, a.isNull = !0
            });
            l.column.prototype.drawPoints.apply(this);
            m(this.data, function (d) {
                d.plotX = a.toPixels(d._midX, !0);
                d.plotY = b.toPixels(d._midY, !0);
                d.isNull && (d[c] = null)
            });
            j.Series.prototype.drawDataLabels.call(this)
        },
        animateDrilldown: function (a) {
            var b = this.chart.plotBox,
                c = this.chart.drilldownLevels[this.chart.drilldownLevels.length - 1],
                d = c.bBox,
                e = this.chart.options.drilldown.animation;
            if (!a) a = Math.min(d.width / b.width, d.height / b.height), c.shapeArgs = {
                scaleX: a,
                scaleY: a,
                translateX: d.x,
                translateY: d.y
            }, m(this.points, function (a) {
                a.graphic.attr(c.shapeArgs).animate({
                    scaleX: 1,
                    scaleY: 1,
                    translateX: 0,
                    translateY: 0
                }, e)
            }), delete this.animate
        },
        animateDrillupFrom: function (a) {
            l.column.prototype.animateDrillupFrom.call(this, a)
        },
        animateDrillupTo: function (a) {
            l.column.prototype.animateDrillupTo.call(this, a)
        }
    });
    q.mapline = p(q.map, {
        lineWidth: 1,
        backgroundColor: "none"
    });
    l.mapline = r(l.map, {
        type: "mapline",
        pointAttrToOptions: {
            stroke: "color",
            "stroke-width": "lineWidth",
            fill: "backgroundColor"
        },
        drawLegendSymbol: l.line.prototype.drawLegendSymbol
    });
    q.mappoint = p(q.scatter, {
        dataLabels: {
            enabled: !0,
            format: "{point.name}",
            color: "black",
            style: {
                textShadow: "0 0 5px white"
            }
        }
    });
    l.mappoint = r(l.scatter, {
        type: "mappoint"
    });
    if (l.bubble) q.mapbubble = p(q.bubble, {
        tooltip: {
            pointFormat: "{point.name}: {point.z}"
        }
    }), l.mapbubble = r(l.bubble, {
        pointClass: r(u, {
            applyOptions: t.prototype.applyOptions
        }),
        xyFromShape: !0,
        type: "mapbubble",
        pointArrayMap: ["z"],
        getMapData: l.map.prototype.getMapData,
        getBox: l.map.prototype.getBox,
        setData: l.map.prototype.setData
    });
    B.topbutton = function (a, b, c, d, e) {
        return E(e, a, b, c, d, e.r, e.r, 0, 0)
    };
    B.bottombutton = function (a, b, c, d, e) {
        return E(e, a, b, c, d, 0, 0, e.r, e.r)
    };
    j.Renderer === F && m(["topbutton", "bottombutton"], function (a) {
        F.prototype.symbols[a] = B[a]
    });
    j.Map = function (a, b) {
        var c = {
            endOnTick: !1,
            gridLineWidth: 0,
            labels: {
                enabled: !1
            },
            lineWidth: 0,
            minPadding: 0,
            maxPadding: 0,
            startOnTick: !1,
            tickWidth: 0,
            title: null
        }, d;
        d = a.series;
        a.series = null;
        a = p({
            chart: {
                panning: "xy"
            },
            xAxis: c,
            yAxis: p(c, {
                reversed: !0
            })
        }, a, {
            chart: {
                type: "map",
                inverted: !1
            }
        });
        a.series = d;
        return new z(a, b)
    }
})(Highcharts);