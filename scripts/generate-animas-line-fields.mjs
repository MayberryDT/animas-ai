#!/usr/bin/env node

import { mkdir, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, "..");
const VIEW_WIDTH = 1600;
const VIEW_HEIGHT = 2200;

const DIRECTIONS = [
  ["Routed Circuit Traces", routedCircuitTraces],
  ["Processor Pin Fan-Out", processorPinFanOut],
  ["Signal Ring Array", signalRingArray],
  ["Angular Data Lanes", angularDataLanes],
  ["Terminal Scan Paths", terminalScanPaths],
  ["Network Bus Weave", networkBusWeave],
  ["Chip Interconnect Field", chipInterconnectField],
  ["Packet Route Mesh", packetRouteMesh],
  ["Diagnostic Vector Field", diagnosticVectorField],
  ["Machine Schematic Channels", machineSchematicChannels],
];

function parseOutputDirectory() {
  const flag = process.argv.indexOf("--output");
  if (flag === -1) return path.join(ROOT, "docs/design/generated");
  if (!process.argv[flag + 1]) throw new Error("--output requires a directory");
  return path.resolve(process.cwd(), process.argv[flag + 1]);
}

function mulberry32(seed) {
  return () => {
    let value = (seed += 0x6d2b79f5);
    value = Math.imul(value ^ (value >>> 15), value | 1);
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
    return ((value ^ (value >>> 14)) >>> 0) / 4294967296;
  };
}

function between(random, minimum, maximum) {
  return minimum + random() * (maximum - minimum);
}

function integer(random, minimum, maximum) {
  return Math.floor(between(random, minimum, maximum + 1));
}

function number(value) {
  return Math.round(value * 10) / 10;
}

function pointsPath(points) {
  return points.map(([x, y], index) => `${index ? "L" : "M"}${number(x)} ${number(y)}`).join(" ");
}

function routedCircuitTraces(random) {
  const paths = [];
  for (let index = 0; index < 150; index += 1) {
    const fromLeft = index % 2 === 0;
    const startX = fromLeft ? -80 : VIEW_WIDTH + 80;
    const endX = fromLeft ? VIEW_WIDTH + 80 : -80;
    const y = 16 + index * 14.6;
    const x1 = between(random, 160, 560);
    const x2 = between(random, 700, 1040);
    const x3 = between(random, 1160, 1480);
    const jog = integer(random, -5, 5) * 11;
    const ordered = fromLeft ? [x1, x2, x3] : [VIEW_WIDTH - x1, VIEW_WIDTH - x2, VIEW_WIDTH - x3].sort((a, b) => b - a);
    paths.push(pointsPath([
      [startX, y], [ordered[0], y], [ordered[0] + (fromLeft ? 22 : -22), y + jog],
      [ordered[1], y + jog], [ordered[1] + (fromLeft ? 22 : -22), y], [ordered[2], y], [endX, y],
    ]));
  }
  for (let index = 0; index < 48; index += 1) {
    const x = 24 + index * 33;
    const y = integer(random, 4, 89) * 22;
    const height = integer(random, 2, 7) * 22;
    paths.push(pointsPath([[x, y], [x, y + height], [x + (index % 2 ? 22 : -22), y + height + 22]]));
  }
  return paths;
}

function processorPinFanOut(random) {
  const paths = [];
  const chips = [
    [260, 330, 300, 360], [1020, 250, 300, 420], [410, 1180, 340, 410], [1060, 1390, 300, 380],
  ];
  for (const [chipX, chipY, chipWidth, chipHeight] of chips) {
    paths.push(`M${chipX} ${chipY}H${chipX + chipWidth}V${chipY + chipHeight}H${chipX}Z`);
    for (let pin = 0; pin < 24; pin += 1) {
      const y = chipY + 12 + (pin * (chipHeight - 24)) / 23;
      const spread = (pin - 11.5) * 13;
      paths.push(pointsPath([[chipX, y], [chipX - 34, y], [chipX - 82, y + spread], [-80, y + spread]]));
      paths.push(pointsPath([[chipX + chipWidth, y], [chipX + chipWidth + 34, y], [chipX + chipWidth + 82, y - spread], [VIEW_WIDTH + 80, y - spread]]));
    }
    for (let pin = 0; pin < 16; pin += 1) {
      const x = chipX + 14 + (pin * (chipWidth - 28)) / 15;
      const spread = (pin - 7.5) * 12;
      paths.push(pointsPath([[x, chipY], [x, chipY - 34], [x + spread, chipY - 74], [x + spread, chipY - 170]]));
    }
  }
  return paths;
}

function signalRingArray(random) {
  const paths = [];
  const centers = [[220, 260], [790, 310], [1350, 500], [410, 920], [1080, 1120], [230, 1670], [820, 1780], [1390, 1880]];
  for (let centerIndex = 0; centerIndex < centers.length; centerIndex += 1) {
    const [cx, cy] = centers[centerIndex];
    for (let ring = 1; ring <= 23; ring += 1) {
      const rx = ring * (8.8 + (centerIndex % 3));
      const ry = ring * (7.1 + ((centerIndex + 1) % 3));
      const gap = 0.3 + (ring % 5) * 0.08;
      const start = -Math.PI * 0.9 + gap;
      const end = Math.PI * 0.9 - gap;
      const startX = cx + Math.cos(start) * rx;
      const startY = cy + Math.sin(start) * ry;
      const endX = cx + Math.cos(end) * rx;
      const endY = cy + Math.sin(end) * ry;
      paths.push(`M${number(startX)} ${number(startY)}A${number(rx)} ${number(ry)} 0 1 1 ${number(endX)} ${number(endY)}`);
    }
    for (let ray = 0; ray < 6; ray += 1) {
      const angle = (ray / 6) * Math.PI * 2 + between(random, -0.08, 0.08);
      paths.push(pointsPath([[cx + Math.cos(angle) * 18, cy + Math.sin(angle) * 18], [cx + Math.cos(angle) * 210, cy + Math.sin(angle) * 170]]));
    }
  }
  return paths;
}

function angularDataLanes(random) {
  const paths = [];
  for (let index = 0; index < 190; index += 1) {
    const y = -220 + index * 13.6;
    const shiftA = integer(random, -5, 5) * 12;
    const shiftB = integer(random, -6, 6) * 11;
    paths.push(pointsPath([
      [-120, y], [260, y + 190], [420, y + 190 + shiftA], [700, y + 330 + shiftA],
      [910, y + 330 + shiftB], [1260, y + 505 + shiftB], [1720, y + 505],
    ]));
  }
  return paths;
}

function terminalScanPaths(random) {
  const paths = [];
  for (let row = 0; row < 118; row += 1) {
    const y = 18 + row * 18.5;
    let x = -40;
    while (x < VIEW_WIDTH) {
      const width = between(random, 100, 270);
      const jog = integer(random, -2, 2) * 9;
      const end = Math.min(x + width, VIEW_WIDTH + 40);
      paths.push(pointsPath([[x, y], [end - 22, y], [end, y + jog]]));
      x = end + between(random, 18, 64);
    }
  }
  return paths;
}

function networkBusWeave(random) {
  const paths = [];
  for (let bus = 0; bus < 12; bus += 1) {
    const baseY = 80 + bus * 178;
    const pivotA = between(random, 260, 510);
    const pivotB = between(random, 700, 980);
    const pivotC = between(random, 1120, 1430);
    const liftA = integer(random, -4, 4) * 24;
    const liftB = integer(random, -5, 5) * 24;
    for (let lane = 0; lane < 16; lane += 1) {
      const offset = (lane - 7.5) * 8;
      paths.push(pointsPath([
        [-80, baseY + offset], [pivotA, baseY + offset], [pivotA + 32, baseY + liftA + offset],
        [pivotB, baseY + liftA + offset], [pivotB + 32, baseY + liftB + offset],
        [pivotC, baseY + liftB + offset], [pivotC + 32, baseY + offset], [1680, baseY + offset],
      ]));
    }
  }
  return paths;
}

function chipInterconnectField(random) {
  const paths = [];
  const modules = [
    [120, 170, 270, 250], [650, 120, 310, 230], [1170, 300, 260, 280],
    [300, 840, 300, 260], [900, 770, 340, 300], [110, 1540, 290, 280],
    [620, 1460, 300, 250], [1160, 1600, 300, 270],
  ];
  for (const [x, y, width, height] of modules) {
    paths.push(`M${x} ${y}H${x + width}V${y + height}H${x}Z`);
    paths.push(`M${x + 18} ${y + 18}H${x + width - 18}V${y + height - 18}H${x + 18}Z`);
    for (let pin = 0; pin < 20; pin += 1) {
      const side = pin % 4;
      const t = (Math.floor(pin / 4) + 1) / 6;
      let start;
      let end;
      if (side === 0) { start = [x + width * t, y]; end = [start[0] + integer(random, -4, 4) * 24, y - between(random, 80, 250)]; }
      if (side === 1) { start = [x + width, y + height * t]; end = [x + width + between(random, 100, 310), start[1] + integer(random, -4, 4) * 22]; }
      if (side === 2) { start = [x + width * t, y + height]; end = [start[0] + integer(random, -4, 4) * 24, y + height + between(random, 80, 250)]; }
      if (side === 3) { start = [x, y + height * t]; end = [x - between(random, 100, 310), start[1] + integer(random, -4, 4) * 22]; }
      const middle = side % 2 === 0 ? [start[0], end[1]] : [end[0], start[1]];
      paths.push(pointsPath([start, middle, end]));
    }
  }
  return paths;
}

function packetRouteMesh(random) {
  const paths = [];
  const columns = 11;
  const rows = 16;
  const nodes = [];
  for (let row = 0; row < rows; row += 1) {
    for (let column = 0; column < columns; column += 1) {
      nodes.push([
        70 + column * 148 + integer(random, -3, 3) * 9,
        60 + row * 140 + integer(random, -3, 3) * 9,
      ]);
    }
  }
  for (let index = 0; index < nodes.length; index += 1) {
    const [x, y] = nodes[index];
    paths.push(`M${x - 8} ${y}H${x + 8}M${x} ${y - 8}V${y + 8}`);
    if (index % columns < columns - 1) {
      const [endX, endY] = nodes[index + 1];
      const pivot = x + (endX - x) * between(random, 0.28, 0.72);
      paths.push(pointsPath([[x + 8, y], [pivot, y], [pivot, endY], [endX - 8, endY]]));
    }
    if (index + columns < nodes.length && index % 3 === 0) {
      const [endX, endY] = nodes[index + columns];
      paths.push(pointsPath([[x, y + 8], [x + 24, y + 32], [endX + 24, endY - 32], [endX, endY - 8]]));
    }
  }
  return paths;
}

function diagnosticVectorField(random) {
  const paths = [];
  const columns = 23;
  const rows = 29;
  for (let row = 0; row < rows; row += 1) {
    for (let column = 0; column < columns; column += 1) {
      const x = 26 + column * 70 + (row % 2) * 35;
      const y = 30 + row * 76;
      const angle = Math.sin(column * 0.46) * 0.7 + Math.cos(row * 0.31) * 0.55 + between(random, -0.08, 0.08);
      const length = 20 + ((row + column) % 5) * 6;
      const dx = Math.cos(angle) * length;
      const dy = Math.sin(angle) * length;
      paths.push(`M${number(x - dx)} ${number(y - dy)}L${number(x + dx)} ${number(y + dy)}`);
    }
  }
  return paths;
}

function machineSchematicChannels(random) {
  const paths = [];
  for (let band = 0; band < 18; band += 1) {
    const top = 26 + band * 121;
    for (let lane = 0; lane < 9; lane += 1) {
      const y = top + lane * 9;
      const insetA = 90 + ((band * 83 + lane * 29) % 420);
      const insetB = 960 + ((band * 71 + lane * 37) % 470);
      const shift = integer(random, -3, 3) * 18;
      paths.push(pointsPath([[-60, y], [insetA, y], [insetA + 28, y + shift], [insetB, y + shift], [insetB + 28, y], [1660, y]]));
    }
    paths.push(`M${180 + (band % 4) * 310} ${top - 18}V${top + 96}H${320 + (band % 4) * 310}`);
  }
  return paths;
}

function renderSvg(title, subpaths) {
  const chunks = [];
  for (let index = 0; index < subpaths.length; index += 18) chunks.push(subpaths.slice(index, index + 18));
  const paths = chunks.map((chunk) =>
    `  <path d="${chunk.join(" ")}" fill="none" stroke="#2563eb" stroke-opacity="0.08" stroke-width="1" vector-effect="non-scaling-stroke" stroke-linecap="square" stroke-linejoin="miter"/>`
  ).join("\n");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${VIEW_WIDTH} ${VIEW_HEIGHT}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <title>${title}</title>
${paths}
</svg>
`;
}

const outputDirectory = parseOutputDirectory();
const defaultOutputDirectory = path.join(ROOT, "docs/design/generated");
await mkdir(outputDirectory, { recursive: true });
let selectedProductionSvg = "";

for (let index = 0; index < DIRECTIONS.length; index += 1) {
  const [name, generator] = DIRECTIONS[index];
  const random = mulberry32(4109 + index * 1009);
  const svg = renderSvg(name, generator(random));
  const filename = `animas-line-field-${String(index + 1).padStart(2, "0")}.svg`;
  await writeFile(path.join(outputDirectory, filename), svg, "utf8");
  if (filename === "animas-line-field-05.svg") selectedProductionSvg = svg;
  process.stdout.write(`${filename}  ${name}\n`);
}

if (outputDirectory === defaultOutputDirectory && selectedProductionSvg) {
  const productionDirectory = path.join(ROOT, "assets");
  await mkdir(productionDirectory, { recursive: true });
  await writeFile(
    path.join(productionDirectory, "animas-line-field-05.svg"),
    selectedProductionSvg,
    "utf8",
  );
}
