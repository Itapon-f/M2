/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_do_rotate_rev.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 00:00:00 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/01 05:17:49 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rra(t_stack **a, int w)
{
	if (!a || !*a || !(*a)->next || (*a)->next == *a)
		return ;
	*a = (*a)->prev;
	if (w)
		ft_putstr("rra\n");
}

void	ft_rrb(t_stack **b, int w)
{
	if (!b || !*b || !(*b)->next || (*b)->next == *b)
		return ;
	*b = (*b)->prev;
	if (w)
		ft_putstr("rrb\n");
}

void	ft_rrr(t_stack **a, t_stack **b, int w)
{
	ft_rra(a, 0);
	ft_rrb(b, 0);
	if (w)
		ft_putstr("rrr\n");
}

void	ft_execute_rotate_rev(t_stack **from, t_stack **to,
	int from_down, int to_down)
{
	while (from_down > 0 && to_down > 0)
	{
		ft_rrr(from, to, 1);
		from_down--;
		to_down--;
	}
	while (from_down > 0)
	{
		ft_rra(from, 1);
		from_down--;
	}
	while (to_down > 0)
	{
		ft_rrb(to, 1);
		to_down--;
	}
}
